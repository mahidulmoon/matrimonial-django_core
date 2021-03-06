# Generated by Django 3.1.1 on 2020-09-22 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=128)),
                ('lastname', models.CharField(max_length=128)),
                ('sex', models.CharField(max_length=12)),
                ('dob_day', models.CharField(max_length=12)),
                ('dob_month', models.CharField(max_length=28)),
                ('dob_year', models.CharField(max_length=12)),
                ('religion', models.CharField(max_length=28)),
                ('caste', models.CharField(max_length=28)),
                ('subcaste', models.CharField(max_length=28)),
                ('country', models.CharField(max_length=28)),
                ('state', models.CharField(max_length=28)),
                ('district', models.CharField(max_length=28)),
                ('age', models.CharField(max_length=3)),
                ('maritalstatus', models.CharField(max_length=28)),
                ('profileby', models.CharField(max_length=28)),
                ('education', models.CharField(max_length=28)),
                ('specialization', models.CharField(max_length=28)),
                ('bodytype', models.CharField(max_length=28)),
                ('physicalstatus', models.CharField(max_length=28)),
                ('drink', models.CharField(max_length=28)),
                ('smoke', models.CharField(max_length=28)),
                ('mothertounge', models.CharField(max_length=28)),
                ('bloodgroup', models.CharField(max_length=28)),
                ('weight', models.CharField(max_length=28)),
                ('height', models.CharField(max_length=28)),
                ('colour', models.CharField(max_length=28)),
                ('diet', models.CharField(max_length=28)),
                ('occupation', models.CharField(max_length=28)),
                ('occupationdescr', models.CharField(max_length=28)),
                ('income', models.CharField(max_length=28)),
                ('fatheroccupation', models.CharField(max_length=28)),
                ('motheroccupation', models.CharField(max_length=28)),
                ('sis', models.CharField(max_length=28)),
                ('bros', models.CharField(max_length=28)),
                ('aboutme', models.TextField()),
                ('image', models.ImageField(default='images/logo.png', upload_to='images/profile/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
