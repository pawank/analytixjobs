# Generated by Django 2.2 on 2019-04-26 11:36

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190426_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='primary_phone_no',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]