# Generated by Django 5.0.2 on 2024-03-12 10:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agencies', '0002_initial'),
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetail',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='data_custodian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects_where_data_custodian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='modifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects_owned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='projects.project'),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agencies.departmentalservice'),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='site_custodian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects_where_site_custodian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectmember',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='projects.project'),
        ),
        migrations.AddField(
            model_name='projectmember',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_of', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studentprojectdetails',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_project_info', to='projects.project'),
        ),
        migrations.AlterUniqueTogether(
            name='projectmember',
            unique_together={('project', 'user')},
        ),
    ]
