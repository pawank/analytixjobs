# Generated by Django 2.2 on 2019-04-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20190426_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='alt_phone_no',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='Alternate Phone No'),
        ),
        migrations.AddField(
            model_name='employer',
            name='primary_phone_no',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Phone No'),
        ),
    ]
