# Generated by Django 3.1.7 on 2021-03-24 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0003_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='eduYear',
            field=models.PositiveIntegerField(),
        ),
    ]
