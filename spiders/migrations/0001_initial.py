# Generated by Django 2.1 on 2020-07-28 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeiZiTu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NewsDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newstime', models.CharField(max_length=30)),
                ('newurl', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
