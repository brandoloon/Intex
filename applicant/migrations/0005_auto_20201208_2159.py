# Generated by Django 3.1.4 on 2020-12-09 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0004_applicant_about_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='cover_picture',
            field=models.ImageField(blank=True, default='cover_picture/cover-pattern.jpg', upload_to='cover_picture/'),
        ),
    ]
