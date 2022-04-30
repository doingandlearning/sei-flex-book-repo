# Generated by Django 4.0.4 on 2022-04-30 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('books', '0016_book_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='locations',
            field=models.ManyToManyField(blank=True, related_name='books_of_locations', to='locations.location'),
        ),
    ]