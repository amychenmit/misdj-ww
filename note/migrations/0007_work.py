# Generated by Django 2.2.6 on 2019-10-14 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0006_auto_20191012_0248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_num', models.IntegerField()),
                ('date1', models.DateField(verbose_name='Date')),
                ('worker', models.IntegerField()),
            ],
        ),
    ]
