from django.contrib import admin

from debt_payment.models import DeptPayment


class DeptPaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_client', 'id_user', 'id_debtSales', 'sum', 'date')
    search_fields = ('date',)


admin.site.register(DeptPayment, DeptPaymentAdmin)
