# Generated by Django 2.1.5 on 2022-03-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_branch_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='status',
            field=models.CharField(default='Inactive', max_length=10),
        ),
    ]
