from django import forms

from user_app.models import UserCrud


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = UserCrud
        fields = ('first_name', 'last_name', 'iban')
