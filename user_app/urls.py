from django.urls import path

from user_app.views import BasicCrudUpdate, BasicCrudView, create_crud_view


urlpatterns = [
    path('view-crud/', BasicCrudView.as_view(), name='view-crud'),
    path('update-crud/<slug:pk>', BasicCrudUpdate.as_view(), name='update-crud'),
    path('create-crud/', create_crud_view, name='create-crud'),
]
