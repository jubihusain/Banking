# Generated by Django 4.1.6 on 2023-02-12 21:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0011_rename_country_branch_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 2, 13, 3, 26, 41, 731028), null=True),
        ),
    ]
