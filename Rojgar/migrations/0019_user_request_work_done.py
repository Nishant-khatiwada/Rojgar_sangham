# Generated by Django 5.0 on 2023-12-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rojgar', '0018_remove_user_request_work_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_request',
            name='work_done',
            field=models.BooleanField(default=False),
        ),
    ]