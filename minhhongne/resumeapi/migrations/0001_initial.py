# Generated by Django 3.1.3 on 2020-11-09 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('exp_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('overview', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('skill_name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='skills', to='resumeapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Experience',
            fields=[
                ('project_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('overview', models.CharField(max_length=255)),
                ('duties', models.CharField(max_length=500)),
                ('exp', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects', to='resumeapi.experience')),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='experiences', to='resumeapi.user'),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('edu_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('program', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='educations', to='resumeapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('contact_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('linkedin', models.CharField(max_length=255)),
                ('github', models.CharField(max_length=255)),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='info', to='resumeapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('award_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=255)),
                ('award_name', models.CharField(max_length=255)),
                ('award_year', models.CharField(max_length=5)),
                ('description', models.CharField(max_length=255)),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='awards', to='resumeapi.user')),
            ],
        ),
    ]
