# Generated by Django 4.1.2 on 2022-10-28 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images')),
                ('tail', models.CharField(max_length=200)),
            ],
        ),
    ]
