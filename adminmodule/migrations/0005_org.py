# Generated by Django 2.1.5 on 2022-02-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0004_auto_20220222_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('otype', models.CharField(max_length=20)),
                ('doj', models.DateField(auto_now=True, verbose_name='')),
            ],
        ),
    ]
