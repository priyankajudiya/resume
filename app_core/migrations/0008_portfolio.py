# Generated by Django 3.1.7 on 2021-03-25 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0007_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='img/portfolio')),
                ('url', models.URLField(blank=True, null=True)),
                ('date', models.DateField()),
                ('desc', models.CharField(max_length=500)),
                ('technology', models.CharField(blank=True, max_length=256, null=True)),
                ('portFor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_core.profile')),
            ],
        ),
    ]