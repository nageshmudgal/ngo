# Generated by Django 2.1.5 on 2022-03-10 18:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0007_auto_20220301_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.CharField(default='active', max_length=10),
        ),
    ]
