# Generated by Django 2.2.10 on 2020-02-07 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200206_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='interet',
        ),
        migrations.AddField(
            model_name='profil',
            name='interet',
            field=models.ManyToManyField(blank=True, related_name='blabla', to='blog.Profil'),
        ),
    ]
