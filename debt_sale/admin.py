from django.contrib import admin

from debt_sale.models import DebtSale


class DeptSaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_product', 'id_client', 'price', 'created_date', 'debt', 'status')
    search_fields = ('date',)


admin.site.register(DebtSale, DeptSaleAdmin)
