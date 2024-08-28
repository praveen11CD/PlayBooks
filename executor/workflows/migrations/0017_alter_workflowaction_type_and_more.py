# Generated by Django 4.1.13 on 2024-08-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0016_remove_workflowexecutionlog_scheduled_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflowaction',
            name='type',
            field=models.IntegerField(choices=[(0, 'UNKNOWN'), (1, 'API'), (2, 'SLACK_MESSAGE'), (3, 'SLACK_THREAD_REPLY'), (4, 'MS_TEAMS_MESSAGE_WEBHOOK'), (5, 'PAGERDUTY_NOTES'), (6, 'SMTP_EMAIL'), (8, 'ROOTLY_TIMELINE_EVENTS')], db_index=True),
        ),
        migrations.AlterField(
            model_name='workflowentrypoint',
            name='type',
            field=models.IntegerField(choices=[(0, 'UNKNOWN'), (1, 'API'), (2, 'SLACK_CHANNEL_ALERT'), (3, 'PAGERDUTY_INCIDENT'), (5, 'ROOTLY_INCIDENT')], db_index=True),
        ),
    ]
