# Generated by Django 3.2.7 on 2021-09-14 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0008_tvshowproxy_tvshowseasonproxy'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='type',
            field=models.CharField(choices=[('MOV', 'Movie'), ('TVS', 'TV Show'), ('SEA', 'Season'), ('PLY', 'Playlist')], default='PLY', max_length=3),
        ),
    ]
