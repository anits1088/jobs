# Generated by Django 2.2.4 on 2020-02-19 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0005_auto_20200218_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatesprofile',
            name='cover',
            field=models.ImageField(default='0', upload_to='covers'),
        ),
    ]