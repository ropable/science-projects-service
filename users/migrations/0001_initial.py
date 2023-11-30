# Generated by Django 4.2.6 on 2023-11-30 04:35

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agencies', '0001_initial'),
        ('medias', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, verbose_name='username')),
                ('first_name', models.CharField(blank=True, help_text='First name or given name.', max_length=100, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, help_text='Last name or surname.', max_length=100, null=True, verbose_name='Last Name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email address')),
                ('old_pk', models.BigIntegerField(blank=True, help_text='The primary key used in the outdated SPMS', null=True, verbose_name='Old Primary Key')),
                ('is_biometrician', models.BooleanField(default=False, help_text='Whether this user can act as a biometrician if not an admin')),
                ('is_herbarium_curator', models.BooleanField(default=False, help_text='Whether this user can act as a herbarium curator if not an admin')),
                ('is_aec', models.BooleanField(default=False, help_text='Whether this user can act as animal ethics committee if not an admin')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(blank=True, default='None', max_length=30, null=True)),
                ('affiliation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agencies.affiliation')),
                ('agency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agencies.agency')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agencies.branch')),
                ('business_area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agencies.businessarea')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='work', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Work Detail',
                'verbose_name_plural': 'User Work Details',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, choices=[('mr', 'Mr.'), ('ms', 'Ms.'), ('mrs', 'Mrs.'), ('master', 'Master'), ('dr', 'Dr.')], max_length=20, null=True)),
                ('middle_initials', models.CharField(blank=True, max_length=10, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('curriculum_vitae', models.TextField(blank=True, null=True)),
                ('expertise', models.CharField(blank=True, max_length=140, null=True)),
                ('image', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='medias.useravatar')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]
