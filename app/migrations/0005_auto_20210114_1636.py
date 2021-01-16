# Generated by Django 2.2.17 on 2021-01-14 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_software_technical'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='linkedin',
        ),
        migrations.AddField(
            model_name='profile',
            name='blog',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='blog'),
        ),
        migrations.AddField(
            model_name='profile',
            name='youtube',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='youtube'),
        ),
    ]
