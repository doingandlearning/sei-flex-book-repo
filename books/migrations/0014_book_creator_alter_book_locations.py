# Generated by Django 4.0.4 on 2022-04-23 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0001_initial'),
        ('books', '0013_book_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='locations',
            field=models.ManyToManyField(blank=True, related_name='books_set_here', to='locations.location'),
        ),
    ]
