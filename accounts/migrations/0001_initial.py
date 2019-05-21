# Generated by Django 2.2.1 on 2019-05-21 18:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=500)),
                ('picture', models.TextField()),
                ('user', models.ForeignKey(on_delete=False, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
