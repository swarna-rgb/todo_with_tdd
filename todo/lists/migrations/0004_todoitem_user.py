# Generated by Django 3.0.6 on 2020-05-26 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lists.User'),
        ),
    ]