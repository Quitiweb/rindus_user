from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from user_app.forms import CustomUserForm
from user_app.models import UserCrud


class BasicCrudUpdate(UpdateView):
    model = UserCrud
    fields = ['first_name', 'last_name', 'iban']
    template_name = 'update-crud.html'
    success_url = "/thanks/"


class BasicCrudView(ListView):
    model = UserCrud
    template_name = 'view-crud.html'


def create_crud_view(request):
    template = loader.get_template('create-crud.html')

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
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
        form = CustomUserForm()

    return HttpResponse(template.render({'form': form}, request))
