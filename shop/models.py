import os

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField

STATUS = (
    ('True', 'True'),
    ('False', 'False'),
)


class Banner(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="images/banners/")
    status = models.CharField(max_length=20, choices=STATUS)

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Country(models.Model):
    country = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Страна Производства'
        verbose_name_plural = 'Страны Производства'

    def __str__(self):
        return self.country


class Brand(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to="images/brands/", blank=True, null=True)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.logo is not None:
            return mark_safe('<img src="{}" height="50" >'.format(self.logo.url))
        else:
            return ""


class Service(models.Model):
    name = models.CharField(blank=True, null=True, max_length=150, verbose_name="Название")
    services = RichTextField(blank=True, null=True, verbose_name="Услуга")

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    DEFAULT_SPECIFICATION = '''
    <table class="table">
	<tbody>
		<tr>
			<td>
			<h5>Модель</h5>
			</td>
			<td>
			<h5>&nbsp;Лео</h5>
			</td>
		</tr>
		<tr>
			<td>
			<p>Высота полотен</p>
			</td>
			<td>
			<h5>2000мм</h5>
			</td>
		</tr>
		<tr>
			<td>
			<p>Ширина</p>
			</td>
			<td>
			<h5>600,700,800,900 мм</h5>
			</td>
		</tr>
	</tbody>
</table>
'''

    KEYWORDS = '''Межкомнатные двери, двери, дверь, комнантые двери'''

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name="Категория")  # many to one relationship
    title = models.CharField(max_length=150, verbose_name="Название")
    image = models.ImageField(upload_to='images/', null=False, verbose_name="Главное Фото двери")
    keywords = models.CharField(max_length=255, null=True, blank=True, default=KEYWORDS, verbose_name="Ключевые слова")
    brand = models.ForeignKey(Brand, verbose_name="Бренд", on_delete=models.CASCADE, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    services = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    description = RichTextField(blank=True, null=True, verbose_name="Описание")
    amount = models.IntegerField(default=0, verbose_name="Количесво")
    specification = RichTextField(blank=True, null=True, verbose_name="Спецификация", default=DEFAULT_SPECIFICATION)
    slug = models.SlugField(null=False, unique=True, verbose_name="Наименование Ссылки")
    status = models.CharField(max_length=10, choices=STATUS, verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Дверь'
        verbose_name_plural = 'Двери'

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height=50 >'.format(self.image.url))
        else:
            return ""

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class DoorType(models.Model):
    type = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Тип двери'
        verbose_name_plural = 'Типы двери'

    def __str__(self):
        return self.type


class RelatedImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, upload_to="images/")

    def filename(self):
        return os.path.basename(self.image.name)

    def __str__(self):
        return self.product.category.name + ": " + self.product.title + ' | ' + os.path.basename(self.image.name)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="80" >'.format(self.image.url))
        else:
            return ""

    class Meta:
        verbose_name = 'Детальная фото'
        verbose_name_plural = 'Детальные фото'


class Color(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images/colors/")

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50" >'.format(self.image.url))
        else:
            return ""

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Sizes(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"

    def __str__(self):
        return self.name


class Variants(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Название")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Цвет")
    type = models.ForeignKey(DoorType, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Тип")
    image = models.ImageField(blank=True, verbose_name="Фото", upload_to="images/", null=True)
    # images = models.OneToOneField(Images, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Фото")
    # image_id = models.IntegerField(blank=True, null=True, default=0)
    quantity = models.IntegerField(default=1, verbose_name="Количество")
    size = models.ManyToManyField(Sizes, verbose_name="Размеры")
    price = models.FloatField(default=0, verbose_name="Цена")
    sale_price = models.FloatField(default=0, verbose_name="Цена по Скидке", null=True, blank=True)

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="80" >'.format(self.image.url))
        else:
            return ""

    def sale_percent(self):
        old_price = int(self.price)
        new_price = int(self.sale_price)
        sale_percent = ((new_price / old_price) - 1) * 100
        return round(sale_percent)


class ProductReview(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250, verbose_name='Отзыв')
    rate = models.IntegerField(default=1, verbose_name='Оценка', )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(str(self.comment)) > 30:
            return self.author.username + " " + self.product.title + " " + str(self.comment)[0:30]
        else:
            return self.author.username + " " + self.product.title + " " + str(self.comment)[0:len(str(self.comment))]


class LikedProducts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Variants, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' - ' + self.product.title


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=40, null=False, blank=False)
    question = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = PhoneNumberField(null=False, blank=False)
    answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, )
    answer = RichTextField()

    def __str__(self):
        if Answer.objects.filter(question__id=self.question.id).exists():
            data = Question.objects.get(id=self.question.id)
            data.answered = True
            data.save()
        return str(self.question.subject)
