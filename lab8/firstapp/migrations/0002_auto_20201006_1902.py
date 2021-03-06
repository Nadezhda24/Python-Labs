# Generated by Django 3.1.2 on 2020-10-06 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.IntegerField()),
                ('name', models.TextField(max_length=25)),
                ('surname', models.TextField(max_length=25)),
                ('secondName', models.TextField(max_length=25)),
                ('birthday', models.DateField(auto_now=True)),
                ('telephone', models.TextField(max_length=11)),
                ('experience', models.IntegerField()),
                ('id_gender', models.CharField(max_length=10)),
                ('discipline', models.TextField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
