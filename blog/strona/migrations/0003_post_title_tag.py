# Generated by Django 4.0.4 on 2022-06-21 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0002_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='moj blog', max_length=200),
        ),
    ]
