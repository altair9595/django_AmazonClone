from django.contrib import admin
from .models import ProductImages , Product , Brand , Review
from django_summernote.admin import SummernoteModelAdmin

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 5

class ProductAdmain(SummernoteModelAdmin):
    list_display = ['name','brand','quantity','price']
    list_filter =['description','brand','quantity','price']
    search_fields = ['name','brand','subtitl','description']
    inlines = (ProductImagesInline,) 
    summernote_fields = '__all__'

     
  






admin.site.register(Product, ProductAdmain)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)
''''''