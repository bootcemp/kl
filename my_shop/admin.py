from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopuated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image_show', 'price', 'available', 'created', 'uploaded']
    list_filter = ['available', 'created', 'uploaded']
    list_ebitable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    def image_show(self, obi):
        if obi.image:
            return mark_safe("<img src='{}' width='60' />".format(obi.image.url))
        return "None"

    image_show.__name__ = "Картинка"
