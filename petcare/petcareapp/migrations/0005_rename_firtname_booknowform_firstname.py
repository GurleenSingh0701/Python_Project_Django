# Generated by Django 4.1 on 2022-08-29 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petcareapp', '0004_booknowform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booknowform',
            old_name='firtname',
            new_name='firstname',
        ),
    ]
