# Generated by Django 2.1.2 on 2018-11-20 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_auto_20181120_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_list',
            field=models.ManyToManyField(blank=True, related_name='students', to='app01.ClassList', verbose_name='已报班级'),
        ),
    ]
