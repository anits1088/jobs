# Generated by Django 2.2.4 on 2020-02-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0006_candidatesprofile_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatesprofile',
            name='cover',
            field=models.FileField(default='0', upload_to='covers'),
        ),
    ]
