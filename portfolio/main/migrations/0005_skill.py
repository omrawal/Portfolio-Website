# Generated by Django 5.0.6 on 2024-06-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_resume_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_title', models.CharField(max_length=200)),
                ('skill_logo_link', models.URLField(blank=True)),
            ],
        ),
    ]
