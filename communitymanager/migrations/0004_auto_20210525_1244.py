# Generated by Django 2.2 on 2021-05-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0003_auto_20210523_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_evenement',
            field=models.DateTimeField(blank=True, null=True, verbose_name="Date de l'evenement"),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]
