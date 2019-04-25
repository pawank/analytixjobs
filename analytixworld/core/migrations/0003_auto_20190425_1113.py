# Generated by Django 2.2 on 2019-04-25 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190425_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='core',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='core',
            name='updated_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
