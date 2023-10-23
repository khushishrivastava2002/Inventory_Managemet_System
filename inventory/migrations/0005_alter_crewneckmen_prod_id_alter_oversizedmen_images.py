# Generated by Django 4.0.3 on 2023-10-02 12:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_dropcutmen_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crewneckmen',
            name='prod_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='oversizedmen',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
