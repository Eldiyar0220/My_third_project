# Generated by Django 3.2.7 on 2021-10-13 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_activation_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='good',
            field=models.BooleanField(default=False),
        ),
    ]
