# Generated by Django 5.0.6 on 2024-06-12 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_skill_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('company_logo_link', models.URLField(blank=True)),
                ('company_website_link', models.URLField(blank=True)),
                ('designation', models.CharField(max_length=200)),
                ('period_and_location', models.CharField(max_length=200)),
                ('rank', models.IntegerField(default=10)),
            ],
        ),
    ]
