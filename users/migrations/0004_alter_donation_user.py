# Generated by Django 4.1 on 2024-02-25 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.basicuser'),
        ),
    ]