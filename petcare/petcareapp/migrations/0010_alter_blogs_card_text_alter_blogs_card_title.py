# Generated by Django 4.1 on 2022-09-01 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petcareapp', '0009_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='card_text',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='card_title',
            field=models.CharField(max_length=10, null=True),
        ),
    ]