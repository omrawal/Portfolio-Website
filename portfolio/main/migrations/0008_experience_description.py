# Generated by Django 5.0.6 on 2024-06-12 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
