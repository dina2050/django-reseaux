# Generated by Django 2.2.10 on 2020-02-07 10:28

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0010_profil_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='interest',
        ),
        migrations.AddField(
            model_name='profil',
            name='interest',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]