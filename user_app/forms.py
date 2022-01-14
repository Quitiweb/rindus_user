from django import forms
from localflavor.generic.forms import IBANFormField

from user_app.models import UserCrud


class CustomUserForm(forms.ModelForm):
    iban = IBANFormField()

    class Meta:
        model = UserCrud
        fields = ('first_name', 'last_name', 'iban')
