# Generated by Django 3.2.7 on 2021-09-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_auto_20210910_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=220, unique=True),
        ),
    ]