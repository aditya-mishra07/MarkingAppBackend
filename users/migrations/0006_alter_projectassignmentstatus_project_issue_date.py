# Generated by Django 4.1.7 on 2024-03-01 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_projectassignmentstatus_project_issue_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectassignmentstatus',
            name='project_issue_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]