# Generated by Django 4.0.4 on 2022-05-02 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_location_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='books',
        ),
    ]
