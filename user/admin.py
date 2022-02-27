from django.contrib import admin

from user.models import Users


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'userName', 'firstName', 'lastName', 'phone', 'registrationDate')


admin.site.register(Users, UserAdmin)
