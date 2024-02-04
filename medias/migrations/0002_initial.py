# Generated by Django 5.0.1 on 2024-02-02 08:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agencies', '0002_initial'),
        ('documents', '0002_initial'),
        ('medias', '0001_initial'),
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='aecendorsementpdf',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aec_endorsement_pdfs_uploaded', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aecendorsementpdf',
            name='endorsement',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='aec_pdf', to='documents.endorsement'),
        ),
        migrations.AddField(
            model_name='agencyimage',
            name='agency',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='agencies.agency'),
        ),
        migrations.AddField(
            model_name='annualreportmedia',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='documents.annualreport'),
        ),
        migrations.AddField(
            model_name='annualreportmedia',
            name='uploader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='annual_report_media_uploaded', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='annualreportpdf',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='annual_report_pdf_generated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='annualreportpdf',
            name='report',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pdf', to='documents.annualreport'),
        ),
        migrations.AddField(
            model_name='businessareaphoto',
            name='business_area',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='agencies.businessarea'),
        ),
        migrations.AddField(
            model_name='businessareaphoto',
            name='uploader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='business_area_photos_uploaded', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectdocumentpdf',
            name='document',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pdf', to='documents.projectdocument'),
        ),
        migrations.AddField(
            model_name='projectdocumentpdf',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdfs', to='projects.project'),
        ),
        migrations.AddField(
            model_name='projectphoto',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='projects.project'),
        ),
        migrations.AddField(
            model_name='projectphoto',
            name='uploader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_photos_uploaded', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='useravatar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avatar', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='annualreportmedia',
            constraint=models.UniqueConstraint(fields=('kind', 'report'), name='unique_media_per_kind_per_year'),
        ),
    ]
