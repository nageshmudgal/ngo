# Generated by Django 2.1.5 on 2022-03-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0008_auto_20220311_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='razorpay_ordid',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
