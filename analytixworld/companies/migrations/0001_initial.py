# Generated by Django 2.2 on 2019-04-25 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('core_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Core')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Company name')),
                ('registered_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Registered Company name')),
                ('no_employees', models.IntegerField(blank=True, null=True, verbose_name='No of Employees')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
            ],
            options={
                'ordering': ('-created_on', 'name'),
            },
            bases=('core.core',),
        ),
    ]
