# Generated by Django 2.2 on 2019-04-25 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('core_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Core')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Job Title')),
                ('info_url', models.URLField(blank=True, null=True, verbose_name='Job Information URL')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employers', to='companies.Company')),
            ],
            options={
                'ordering': ('-created_on', 'title'),
            },
            bases=('core.core',),
        ),
    ]
