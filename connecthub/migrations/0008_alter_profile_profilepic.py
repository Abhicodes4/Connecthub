# Generated by Django 5.0.2 on 2024-03-12 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connecthub', '0007_alter_profile_bio_alter_profile_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilepic',
            field=models.ImageField(blank=True, default='hey there im using connecthub', null=True, upload_to='profile_pic1'),
        ),
    ]