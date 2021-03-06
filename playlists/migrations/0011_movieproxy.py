# Generated by Django 3.2.7 on 2021-09-14 21:38

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0010_alter_playlist_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieProxy',
            fields=[
            ],
            options={
                'verbose_name': 'TV Show',
                'verbose_name_plural': 'TV Shows',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('playlists.playlist',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
