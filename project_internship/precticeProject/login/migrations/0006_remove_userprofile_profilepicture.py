# Generated by Django 2.2.9 on 2020-01-16 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20200116_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profilePicture',
        ),
    ]