# Generated by Django 4.2.6 on 2023-10-26 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0003_alter_agencyimage_file_alter_agencyimage_old_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencyimage',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='user-uploads/'),
        ),
        migrations.AlterField(
            model_name='agencyimage',
            name='old_file',
            field=models.FileField(blank=True, null=True, upload_to='user-uploads/'),
        ),
    ]
