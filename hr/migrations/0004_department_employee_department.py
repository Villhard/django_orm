# Generated by Django 5.1.2 on 2024-11-01 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_contact_employee_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hr.department'),
        ),
    ]
