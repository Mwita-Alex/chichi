# Generated by Django 3.2.8 on 2021-10-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_summary',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='events/images/'),
        ),
    ]
