# Generated by Django 3.0.6 on 2020-07-08 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20200707_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=567134, unique=True),
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='status',
            field=models.CharField(choices=[('enrolled', 'Enrolled'), ('not enrolled', 'Not Enrolled')], default='Not Enrolled', max_length=20),
        ),
    ]
