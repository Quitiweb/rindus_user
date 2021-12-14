# Generated by Django 4.0 on 2021-12-14 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercrud',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_crud', to='auth.user'),
        ),
    ]
