# Generated by Django 4.0.4 on 2022-04-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('books', '0012_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='locations',
            field=models.ManyToManyField(blank=True, to='locations.location'),
        ),
    ]
