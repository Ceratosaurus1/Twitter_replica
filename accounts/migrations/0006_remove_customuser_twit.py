# Generated by Django 4.0.10 on 2024-04-15 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_twit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='twit',
        ),
    ]
