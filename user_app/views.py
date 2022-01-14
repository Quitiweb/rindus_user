from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from user_app.forms import CustomUserCreationForm
from user_app.models import UserCrud


def basic_crud_view(request):
    template = loader.get_template('basic-crud.html')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            iban = form.cleaned_data['iban']

            UserCrud.objects.create(
                owner=request.user,
                first_name=first_name,
                last_name=last_name,
                iban=iban
            )

            return HttpResponseRedirect('/thanks/')

    else:
        form = CustomUserCreationForm()

    return HttpResponse(template.render({'form': form}, request))
