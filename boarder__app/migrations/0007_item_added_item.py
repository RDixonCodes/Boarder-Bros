# Generated by Django 2.2 on 2022-10-18 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boarder__app', '0006_user_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='added_item',
            field=models.ManyToManyField(related_name='added_items', to='boarder__app.User'),
        ),
    ]
