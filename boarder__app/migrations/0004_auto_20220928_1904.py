# Generated by Django 2.2 on 2022-09-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boarder__app', '0003_auto_20220928_0557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='registered_user',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]