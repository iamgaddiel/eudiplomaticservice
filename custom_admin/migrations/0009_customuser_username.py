# Generated by Django 5.0 on 2023-12-19 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_admin', '0008_shipmenthistory_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.TextField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
