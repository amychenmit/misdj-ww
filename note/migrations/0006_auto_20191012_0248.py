# Generated by Django 2.2.6 on 2019-10-12 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_auto_20191010_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yr', models.IntegerField()),
                ('num', models.IntegerField()),
                ('date1', models.DateField(verbose_name='Date From')),
                ('date2', models.DateField(verbose_name='Date To')),
            ],
        ),
        migrations.RenameField(
            model_name='note002',
            old_name='whatever',
            new_name='detail',
        ),
    ]