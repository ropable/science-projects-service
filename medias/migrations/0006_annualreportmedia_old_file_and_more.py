# Generated by Django 4.2.6 on 2023-10-26 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0005_remove_agencyimage_old_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualreportmedia',
            name='old_file',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='businessareaphoto',
            name='old_file',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectdocumentpdf',
            name='old_file',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectphoto',
            name='old_file',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useravatar',
            name='old_file',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agencyimage',
            name='file',
            field=models.FileField(upload_to='agencies/'),
        ),
    ]
