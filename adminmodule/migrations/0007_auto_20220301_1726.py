# Generated by Django 2.1.5 on 2022-03-01 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0006_auto_20220228_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='sdesc',
            field=models.CharField(default='-', max_length=100),
        ),
    ]