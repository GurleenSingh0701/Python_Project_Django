# Generated by Django 4.1 on 2022-09-02 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petcareapp', '0011_alter_blogs_card_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='card_link',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
