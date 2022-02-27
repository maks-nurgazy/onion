from django.contrib import admin

from client.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstName', 'lastName', 'inn', 'lastName', 'phone')
    search_fields = ('lastName', 'inn')


admin.site.register(Client, ClientAdmin)
