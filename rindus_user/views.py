from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class ThanksView(TemplateView):
    template_name = 'thanks.html'
