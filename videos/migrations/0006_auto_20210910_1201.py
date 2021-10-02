# Generated by Django 3.2.7 on 2021-09-10 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_videoallproxy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VideoProxy',
        ),
        migrations.CreateModel(
            name='VideoPublishedProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Published Video',
                'verbose_name_plural': 'Published Videos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('videos.video',),
        ),
    ]