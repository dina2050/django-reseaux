# Generated by Django 2.2.10 on 2020-02-06 14:09

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200206_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='profil',
            name='zipcode',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
