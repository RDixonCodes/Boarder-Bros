# Generated by Django 2.2 on 2022-09-28 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boarder__app', '0005_remove_user_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.ImageField(default=2, upload_to=None),
            preserve_default=False,
        ),
    ]
