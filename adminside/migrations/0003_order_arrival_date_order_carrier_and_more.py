# Generated by Django 5.0.6 on 2024-05-13 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0002_alter_order_tracking_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='arrival_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='carrier',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='departure_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='destination',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='origin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='package',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='reference_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='type_of_shipment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='EXWA049472ea-9de3-47e3-ORDER', max_length=30, unique=True),
        ),
    ]
