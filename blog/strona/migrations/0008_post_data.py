# Generated by Django 4.0.4 on 2022-06-22 09:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0007_remove_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='data',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
