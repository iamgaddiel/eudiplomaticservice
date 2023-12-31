# Generated by Django 5.0 on 2023-12-19 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_admin', '0002_alter_package_shipment_medium'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='total_freight',
        ),
        migrations.AddField(
            model_name='package',
            name='freight_cost',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='height',
            field=models.PositiveIntegerField(default=0, help_text='(IN.)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='length',
            field=models.PositiveIntegerField(default=0, help_text='(IN.)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='width',
            field=models.PositiveIntegerField(default=0, help_text='(IN.)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='package',
            name='weight',
            field=models.PositiveIntegerField(help_text='(LBS.)'),
        ),
    ]
