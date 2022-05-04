import admin_thumbnails
from django.contrib import admin
from shop.models import *


class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = ['name', 'image_tag']


class RelatedImagesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'product', 'image_tag']
    readonly_fields = ('pk',)
    list_filter = ['product']


class DetailsImageInline(admin.TabularInline):
    model = RelatedImages
    readonly_fields = ('pk', 'image_tag')
    extra = 1


class ProductVariantsInline(admin.TabularInline):
    model = Variants
    readonly_fields = ('image_tag',)
    extra = 1
    show_change_link = True


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'image_tag']
    list_filter = ['category', 'status', ]
    readonly_fields = ('image_tag',)
    inlines = [ProductVariantsInline, DetailsImageInline]
    prepopulated_fields = {'slug': ('title',)}


class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'image_tag']


class SizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


class VariantsAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'color', 'price', 'quantity', 'image_tag']
    list_filter = ['product', 'price', 'type', 'color', ]


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'rate', 'comment', 'created_at', 'updated_at', ]
    list_filter = ['product', 'author', 'rate', ]


admin.site.register(Banner)
admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(RelatedImages, RelatedImagesAdmin)
admin.site.register(Sizes)
admin.site.register(DoorType)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Variants, VariantsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
