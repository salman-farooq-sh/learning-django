# Generated by Django 4.0.5 on 2022-06-25 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
    ]