from django.contrib import admin

from user_app import models


@admin.register(models.UserCrud)
class UserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'iban')
    list_display = ('first_name', 'last_name', 'iban')

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.fields + ('owner', )

        return self.fields

    def get_list_display(self, request):
        if request.user.is_superuser:
            return self.list_display + ('owner', )

        return self.list_display

    def get_queryset(self, request):
        """
            If is_superuser: returns everything
            if is_staff: returns only crud_users created by the staff user
        """
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.owner = request.user
        super().save_model(request, obj, form, change)
