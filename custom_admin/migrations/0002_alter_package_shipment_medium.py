# Generated by Django 5.0 on 2023-12-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='shipment_medium',
            field=models.CharField(choices=[('Road', 'Road'), ('Ship', 'Ship'), ('Flight', 'Flight')], max_length=300),
        ),
    ]
