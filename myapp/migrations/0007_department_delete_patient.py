# Generated by Django 4.0 on 2023-08-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_appointment_appointmentdate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
