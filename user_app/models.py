from django.db import models
from django.conf import settings


class UserCrud(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    iban = models.CharField(max_length=50)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='user_crud', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        unique_together = ('first_name', 'last_name')
