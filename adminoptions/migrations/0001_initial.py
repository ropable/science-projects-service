# Generated by Django 5.0.6 on 2024-05-11 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email_options', models.CharField(choices=[('enabled', 'Enabled'), ('admin', 'Admin'), ('disabled', 'Disabled')], default='disabled', max_length=50)),
            ],
            options={
                'verbose_name': 'Admin Controls',
            },
        ),
    ]
