# Generated by Django 5.0.3 on 2024-04-01 13:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twits', '0005_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='twit',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_twits', to=settings.AUTH_USER_MODEL),
        ),
    ]
