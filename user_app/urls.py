from django.urls import path

from user_app.views import basic_crud_view


urlpatterns = [
    path('basic-crud/', basic_crud_view, name='basic-crud'),
]
