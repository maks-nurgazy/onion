from django.contrib import admin

from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'description', 'state')
    search_fields = ('brand', 'model')


admin.site.register(Product, ProductAdmin)
