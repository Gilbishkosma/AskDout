# Generated by Django 2.1 on 2018-08-24 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0008_remove_profile_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='question',
            field=models.ManyToManyField(blank=True, null=True, to='ask.Question'),
        ),
    ]
