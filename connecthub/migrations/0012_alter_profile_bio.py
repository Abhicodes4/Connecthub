# Generated by Django 5.0.2 on 2024-03-12 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connecthub', '0011_alter_profile_bio_alter_profile_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='hey there im using connecthub', max_length=50, null=True),
        ),
    ]
