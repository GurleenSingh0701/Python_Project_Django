# Generated by Django 4.1 on 2022-08-30 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petcareapp', '0005_rename_firtname_booknowform_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booknowform',
            name='email_id',
            field=models.EmailField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='booknowform',
            name='firstname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='booknowform',
            name='lastname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='booknowform',
            name='phone_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
