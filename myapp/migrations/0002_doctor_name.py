# Generated by Django 4.0 on 2023-08-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
