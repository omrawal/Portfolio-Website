# Generated by Django 5.0.6 on 2024-06-12 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_experience_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
