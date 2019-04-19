# Generated by Django 2.2 on 2019-04-19 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Company name')),
                ('registered_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Registered Company name')),
                ('no_employees', models.IntegerField(blank=True, null=True, verbose_name='No of Employees')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
