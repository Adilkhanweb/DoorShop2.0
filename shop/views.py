from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from members.forms import QuestionForm
from shop.filters import *
from shop.forms import *


def test(request):
    # products = Product.objects.all()
    brands = Brand.objects.all()
    variants = Variants.objects.all()
    existing_colors = variants.values('color__name').distinct()
    products = Variants.objects.all().order_by('?')
    variant_filter = VariantsFilter(request.GET, queryset=products)
    return render(request, 'test.html',
                  context={'products': products, 'brands': brands, 'colors': existing_colors, 'filter': variant_filter})


class HomeView(ListView):
    model = Product
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        banners = Banner.objects.all()
        products = Product.objects.filter(status='True')
        brands = Brand.objects.all()
        # newArrivals = Product.objects.filter(created_at__range=(timezone.datetime.today() - timezone.timedelta(days=3), timezone.datetime.today()))
        newArrivals = Product.objects.all()
        roomDoors = Product.objects.filter(category__slug='Mezhkomnatnie-dveri').filter(status='True')
        ironDoors = Product.objects.filter(category__slug='Vhodnie-dveri').filter(status='True')
        categories = Category.objects.all()
        variants = Variants.objects.all()
        existing_colors = variants.values('color__name').distinct()
        context['categories'] = categories
        context['banners'] = banners
        context['variants'] = variants
        context['products'] = products
        context['brands'] = brands
        context['roomDoors'] = roomDoors
        context['ironDoors'] = ironDoors
        context['newArrivals'] = newArrivals
        context['existing_colors'] = existing_colors
        return context


class DoorDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, *args, **kwargs):
        product = Product.objects.get(slug=self.kwargs['slug'])
        reviews = ProductReview.objects.filter(product__slug=self.kwargs['slug']).order_by('-created_at')[0:6]
        products = Product.objects.filter(status='True')
        context = super().get_context_data(**kwargs)
        variants = Variants.objects.filter(product_id=product.id)
        related_images = RelatedImages.objects.filter(product_id=product.id)
        colors = variants.values('color__name').distinct()
        types = variants.values('type__type').distinct()
        categories = Category.objects.all()
        context['categories'] = categories
        context['variants'] = variants
        context['products'] = products
        context['colors'] = colors
        context['types'] = types
        context['reviews'] = reviews
        context['related_images'] = related_images
        return context


# def CategoryPorducts(request, slug):
#     variants = Variants.objects.filter(product__category__slug=slug)
#     context = {}
#     paginated = Paginator(variants, 3)
#     context['paginated'] = paginated


class CategoryProductsView(ListView):
    model = Product
    template_name = 'category_products.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        search_products = Product.objects.filter(status='True')
        variants = Variants.objects.filter(product__category__slug=self.kwargs['slug']).order_by('title')
        if ('Mezhkomnatnie-dveri' == str(self.kwargs['slug'])):
            variant_filter = VariantsFilter(self.request.GET, queryset=variants)
            context['filter'] = variant_filter
            paginated_filtered_products = Paginator(variant_filter.qs, 5)
            page_number = self.request.GET.get('page')
            product_page_obj = paginated_filtered_products.get_page(page_number)

        else:
            ironvars_filter = IronVariantsFilter(self.request.GET, queryset=variants)
            context['filter'] = ironvars_filter
            paginated_filtered_products = Paginator(ironvars_filter.qs, 5)
            page_number = self.request.GET.get('page')
            product_page_obj = paginated_filtered_products.get_page(page_number)

        category_name = variants.first().product.category
        categories = Category.objects.all()
        context['products'] = search_products
        context['category_name'] = category_name
        context['product_page_obj'] = product_page_obj
        context['categories'] = categories
        return context


def AddReviewView(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    # return HttpResponse(url)
    if request.method == 'POST':  # check post
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = ProductReview()  # create relation with model
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.product_id = id
            current_user = request.user
            data.author_id = current_user.id
            data.save()  # save data to table
            messages.success(request, "Ваш отзыв успешно сохранен. Спасибо за отзыв!")
            return HttpResponseRedirect(url)
        else:
            for field in form.errors:
                messages.error(request, field + ': ' + form.errors[field].as_text())
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)


def ChangeReviewView(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    data = get_object_or_404(ProductReview, id=id)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=data)
        if form.is_valid():
            data.rate = form.cleaned_data['rate']
            data.comment = form.cleaned_data['comment']
            form.save()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


def DeleteReviewView(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    # fetch the object related to passed id
    obj = get_object_or_404(ProductReview, id=id)

    if request.method == "POST":
        obj.delete()

        return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)


class LikedProductsView(ListView):
    model = LikedProducts
    template_name = 'liked_products.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        liked_products = LikedProducts.objects.filter(user__pk=self.kwargs['pk'])

        context['liked_products'] = liked_products
        context['categories'] = Category.objects.all()
        return context


def AddToLiked(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    liked = False
    # return HttpResponse(url)
    if request.method == 'POST':  # check post
        data = LikedProducts()  # create relation with model
        if LikedProducts.objects.filter(product_id=id).exists():
            LikedProducts.objects.filter(product_id=id).delete()
            liked = False
            return HttpResponseRedirect(url)
        else:
            data.product_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()  # save data to table
            liked = True

    return HttpResponseRedirect(url)


def ContactView(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    # return HttpResponse(url)
    if request.method == 'POST':  # check post
        form = QuestionForm(request.POST)
        if form.is_valid():
            data = Question()  # create relation with model
            data.subject = form.cleaned_data['subject']
            data.question = form.cleaned_data['question']
            data.phone_number = form.cleaned_data['phone_number']
            if (form.cleaned_data['product']):
                data.product_id = form.cleaned_data['product'].id
            data.user_id = id
            data.save()  # save data to table
            messages.success(request, "Ваш запрос успешно отправлен!")
            return HttpResponseRedirect(url)
        else:
            for field in form.errors:
                messages.error(request, field + ': ' + form.errors[field].as_text())
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)


class MyQuestions(ListView):
    model = Question
    template_name = 'my_questions.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = products
        return context
