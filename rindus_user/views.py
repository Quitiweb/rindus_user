from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.views.generic import TemplateView


@receiver(user_signed_up)
def user_signed_up_(request, user, **kwargs):
    if not user.is_staff:
        user.is_staff = True
        user.save()


class HomeView(TemplateView):
    template_name = 'home.html'
