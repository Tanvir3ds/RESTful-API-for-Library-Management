# Generated by Django 3.0.3 on 2020-03-04 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0018_bookloan_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookloan',
            old_name='order',
            new_name='Accepted',
        ),
    ]