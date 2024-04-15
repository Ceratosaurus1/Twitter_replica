# Generated by Django 4.0.10 on 2024-04-15 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twits', '0007_alter_comment_author_alter_twit_author'),
        ('accounts', '0004_delete_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='twit',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='twits.twit'),
            preserve_default=False,
        ),
    ]
