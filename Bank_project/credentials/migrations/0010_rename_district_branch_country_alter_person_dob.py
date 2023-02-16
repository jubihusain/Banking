# Generated by Django 4.1.6 on 2023-02-12 21:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0009_rename_branch_person_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='district',
            new_name='country',
        ),
        migrations.AlterField(
            model_name='person',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 2, 13, 2, 49, 41, 628916), null=True),
        ),
    ]
