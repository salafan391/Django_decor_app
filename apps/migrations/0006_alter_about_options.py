# Generated by Django 4.1.2 on 2022-10-29 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_alter_about_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': [('text', 'النص'), ('phone', 'رقم الجوال'), ('logo', 'الشعار'), ('address', 'العنوان'), ('url', 'الرابط')]},
        ),
    ]
