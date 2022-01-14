from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from user_app.forms import CustomUserCreationForm


def basic_crud_view(request):
    template = loader.get_template('basic-crud.html')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = CustomUserCreationForm()

    return HttpResponse(template.render({'form': form}, request))
