# Generated by Django 4.0.10 on 2024-04-15 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twits', '0008_twit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twit',
            name='image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
