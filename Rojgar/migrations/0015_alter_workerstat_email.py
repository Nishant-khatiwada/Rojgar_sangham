# Generated by Django 5.0 on 2023-12-21 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rojgar', '0014_remove_workerstat_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerstat',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
