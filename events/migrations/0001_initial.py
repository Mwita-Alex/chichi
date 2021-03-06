# Generated by Django 3.2.8 on 2021-10-25 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='events/images/')),
                ('event_title', models.CharField(blank=True, max_length=100)),
                ('event_date', models.DateTimeField(blank=True)),
                ('event_summary', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]
