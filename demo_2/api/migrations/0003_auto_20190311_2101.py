# Generated by Django 2.1.3 on 2019-03-11 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190311_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
