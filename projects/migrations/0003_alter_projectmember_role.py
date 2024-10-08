# Generated by Django 5.0.6 on 2024-05-18 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmember',
            name='role',
            field=models.CharField(choices=[('supervising', 'Supervising Scientist'), ('research', 'Research Scientist'), ('technical', 'Technical Officer'), ('externalcol', 'External Collaborator'), ('externalpeer', 'External Peer'), ('academicsuper', 'Academic Supervisor'), ('student', 'Supervised Student'), ('consulted', 'Consulted Peer'), ('group', 'Involved Group')], max_length=50),
        ),
    ]
