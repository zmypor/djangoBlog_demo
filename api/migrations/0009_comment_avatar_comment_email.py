# Generated by Django 5.1 on 2024-08-25 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='avatar',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]
