# Generated by Django 2.1 on 2018-08-24 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0010_auto_20180825_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='profile',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profileuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
