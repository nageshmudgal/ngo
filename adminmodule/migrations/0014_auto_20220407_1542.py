# Generated by Django 2.1.5 on 2022-04-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0013_auto_20220313_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='doj',
            field=models.DateField(auto_now=True),
        ),
    ]