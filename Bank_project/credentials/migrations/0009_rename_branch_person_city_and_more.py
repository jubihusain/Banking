# Generated by Django 4.1.6 on 2023-02-12 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0008_alter_person_dob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='branch',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='district',
            new_name='country',
        ),
        migrations.AlterField(
            model_name='person',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 2, 13, 2, 42, 30, 799582), null=True),
        ),
    ]
