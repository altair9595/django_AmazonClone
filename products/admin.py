from django.contrib import admin
from .models import ProductImages , Product , Brand , Review

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 5

class ProductAdmain(admin.ModelAdmin):
    list_display = ['name','brand','quantity','price']
    list_filter =['description','brand','quantity','price']
    search_fields = ['name','brand','subtitl','description']
    inlines = (ProductImagesInline,) 







admin.site.register(Product, ProductAdmain)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)