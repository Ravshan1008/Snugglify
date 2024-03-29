# Generated by Django 4.1 on 2024-02-25 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_manager_shelter'),
        ('pets', '0002_pet_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('is_pending', models.BooleanField(default=True)),
                ('approved', models.BooleanField(default=False)),
                ('adopter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.basicuser')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
        ),
    ]
