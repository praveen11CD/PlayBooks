# Generated by Django 4.1.13 on 2024-05-16 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userinvitation'),
        ('executor', '0021_remove_playbooktaskdefinition_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlayBookExecutionLog',
            new_name='PlayBookTaskExecutionLog',
        ),
    ]
