# Generated by Django 3.2.7 on 2021-09-10 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_alter_videoproxy_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
