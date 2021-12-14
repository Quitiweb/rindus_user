from django.contrib import admin

from user_app import models


@admin.register(models.UserCrud)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'iban')
