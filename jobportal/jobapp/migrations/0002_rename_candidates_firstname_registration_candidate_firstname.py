# Generated by Django 3.2.5 on 2021-07-23 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='Candidates_Firstname',
            new_name='Candidate_Firstname',
        ),
    ]
