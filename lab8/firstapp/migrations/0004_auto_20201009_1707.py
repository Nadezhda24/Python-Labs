# Generated by Django 3.1.2 on 2020-10-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20201009_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birthday',
            field=models.DateField(verbose_name='my date'),
        ),
    ]
