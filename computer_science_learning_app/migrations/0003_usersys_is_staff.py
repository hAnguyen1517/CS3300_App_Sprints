# Generated by Django 4.2.11 on 2024-04-14 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer_science_learning_app', '0002_remove_usersys_password_usersys_last_login_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersys',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
