# Generated by Django 3.2.8 on 2021-10-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_rename_blogs_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='summary',
            new_name='blog_summary',
        ),
        migrations.AddField(
            model_name='blog',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blogs/images/'),
        ),
    ]