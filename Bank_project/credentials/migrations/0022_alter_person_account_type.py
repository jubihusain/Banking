# Generated by Django 4.1.6 on 2023-02-14 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0021_remove_person_gender_alter_person_account_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='account_type',
            field=models.CharField(choices=[('savings', 'Savings'), ('current', 'Current'), ('depoit', 'Depoit'), ('demat', 'Demat')], default='----', max_length=10),
        ),
    ]
