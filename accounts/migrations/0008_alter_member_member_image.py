# Generated by Django 3.2.8 on 2021-11-28 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_member_member_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_image',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/members/images/'),
        ),
    ]
