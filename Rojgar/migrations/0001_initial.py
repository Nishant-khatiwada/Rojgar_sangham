# Generated by Django 5.0 on 2023-12-20 07:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='user_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('selected', models.CharField(max_length=50, null=True)),
                ('problem', models.TextField()),
                ('date', models.DateField()),
                ('is_accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField(null=True)),
                ('accepted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accepted_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]