# Generated by Django 3.0.2 on 2020-05-03 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0055_auto_20200425_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchtvseasonrequest',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
