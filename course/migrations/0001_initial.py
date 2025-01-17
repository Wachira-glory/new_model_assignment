# Generated by Django 5.0.6 on 2024-06-24 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=20)),
                ('course_description', models.CharField(max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('course_code', models.PositiveSmallIntegerField()),
                ('teacher_code', models.PositiveSmallIntegerField()),
                ('course_materials', models.TextField()),
                ('course_attendees', models.PositiveSmallIntegerField()),
                ('course_fee', models.CharField(max_length=20)),
            ],
        ),
    ]
