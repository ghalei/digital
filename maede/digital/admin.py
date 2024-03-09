from django.contrib import admin
from .models import Category,Product,Productfile

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display=['title','is_enable']

class ProductfileInlineAdmin(admin.StackedInline):
    model=Productfile
    fields=['title','file']
    extra=0


@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):

  list_display=['title','is_enable']