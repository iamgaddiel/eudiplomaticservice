# Generated by Django 5.0 on 2023-12-19 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_admin', '0007_alter_shipmenthistory_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipmenthistory',
            name='date',
            field=models.DateField(default='2023-12-29'),
            preserve_default=False,
        ),
    ]
