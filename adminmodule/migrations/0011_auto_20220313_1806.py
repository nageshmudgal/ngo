# Generated by Django 2.1.5 on 2022-03-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0010_auto_20220312_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donations',
            old_name='razorpay_ordid',
            new_name='razorpay_order_id',
        ),
        migrations.AddField(
            model_name='donations',
            name='payment_status',
            field=models.IntegerField(choices=[(1, 'SUCCESS'), (2, 'FAILURE'), (3, 'PENDING')], default=3),
        ),
        migrations.AddField(
            model_name='donations',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='donations',
            name='razorpay_signature',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
