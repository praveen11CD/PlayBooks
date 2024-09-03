# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/playbooks/workflow.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from protos import base_pb2 as protos_dot_base__pb2
from protos.playbooks import deprecated_playbook_pb2 as protos_dot_playbooks_dot_deprecated__playbook__pb2
from protos.playbooks import playbook_pb2 as protos_dot_playbooks_dot_playbook__pb2
from protos.playbooks.workflow_schedules import cron_schedule_pb2 as protos_dot_playbooks_dot_workflow__schedules_dot_cron__schedule__pb2
from protos.playbooks.workflow_schedules import interval_schedule_pb2 as protos_dot_playbooks_dot_workflow__schedules_dot_interval__schedule__pb2
from protos.playbooks.workflow_schedules import one_off_schedule_pb2 as protos_dot_playbooks_dot_workflow__schedules_dot_one__off__schedule__pb2
from protos.playbooks.workflow_entry_points import slack_alert_entry_point_pb2 as protos_dot_playbooks_dot_workflow__entry__points_dot_slack__alert__entry__point__pb2
from protos.playbooks.workflow_entry_points import pd_incident_entry_point_pb2 as protos_dot_playbooks_dot_workflow__entry__points_dot_pd__incident__entry__point__pb2
from protos.playbooks.workflow_entry_points import rootly_incident_entry_point_pb2 as protos_dot_playbooks_dot_workflow__entry__points_dot_rootly__incident__entry__point__pb2
from protos.playbooks.workflow_entry_points import zd_incident_entry_point_pb2 as protos_dot_playbooks_dot_workflow__entry__points_dot_zd__incident__entry__point__pb2
from protos.playbooks.workflow_entry_points import api_entry_point_pb2 as protos_dot_playbooks_dot_workflow__entry__points_dot_api__entry__point__pb2
from protos.playbooks.workflow_actions import api_trigger_pb2 as protos_dot_playbooks_dot_workflow__actions_dot_api__trigger__pb2
from protos.playbooks.workflow_actions import slack_message_pb2 as protos_dot_playbooks_dot_workflow__actions_dot_slack__message__pb2
from protos.playbooks.workflow_actions import slack_thread_reply_pb2 as protos_dot_playbooks_dot_workflow__actions_dot_slack__thread__reply__pb2
from protos.playbooks.workflow_actions import pd_notes_pb2 as protos_dot_playbooks_dot_workflow__actions_dot_pd__notes__pb2
from protos.playbooks.workflow_actions import rootly_timeline_events_pb2 as protos_dot_playbooks_dot_workflow__actions_dot_rootly__timeline__events__pb2
from protos.playbooks.workflow_actions import zenduty_notes_pb2 as protos_dot_playbooks_dot_workflow__actions_dot_zenduty__notes__pb2
from protos.playbooks.workflow_actions import ms_teams_message_webhook_pb2 as protos_dot_playbooks_dot_workflow__actions_dot_ms__teams__message__webhook__pb2
from protos.playbooks.workflow_actions import smtp_email_pb2 as protos_dot_playbooks_dot_workflow__actions_dot_smtp__email__pb2
from protos.playbooks.source_task_definitions import lambda_function_task_pb2 as protos_dot_playbooks_dot_source__task__definitions_dot_lambda__function__task__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fprotos/playbooks/workflow.proto\x12\x10protos.playbooks\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x11protos/base.proto\x1a*protos/playbooks/deprecated_playbook.proto\x1a\x1fprotos/playbooks/playbook.proto\x1a\x37protos/playbooks/workflow_schedules/cron_schedule.proto\x1a;protos/playbooks/workflow_schedules/interval_schedule.proto\x1a:protos/playbooks/workflow_schedules/one_off_schedule.proto\x1a\x44protos/playbooks/workflow_entry_points/slack_alert_entry_point.proto\x1a\x44protos/playbooks/workflow_entry_points/pd_incident_entry_point.proto\x1aHprotos/playbooks/workflow_entry_points/rootly_incident_entry_point.proto\x1a\x44protos/playbooks/workflow_entry_points/zd_incident_entry_point.proto\x1a<protos/playbooks/workflow_entry_points/api_entry_point.proto\x1a\x33protos/playbooks/workflow_actions/api_trigger.proto\x1a\x35protos/playbooks/workflow_actions/slack_message.proto\x1a:protos/playbooks/workflow_actions/slack_thread_reply.proto\x1a\x30protos/playbooks/workflow_actions/pd_notes.proto\x1a>protos/playbooks/workflow_actions/rootly_timeline_events.proto\x1a\x35protos/playbooks/workflow_actions/zenduty_notes.proto\x1a@protos/playbooks/workflow_actions/ms_teams_message_webhook.proto\x1a\x32protos/playbooks/workflow_actions/smtp_email.proto\x1a\x43protos/playbooks/source_task_definitions/lambda_function_task.proto\"\x8f\x02\n\x15WorkflowConfiguration\x12\x34\n\x10generate_summary\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\x13global_variable_set\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x46\n\x1btransformer_lambda_function\x18\x03 \x01(\x0b\x32!.protos.playbooks.Lambda.Function\x12\x42\n\x1c\x65valuation_window_in_seconds\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\"\xad\x02\n\x10WorkflowSchedule\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\'.protos.playbooks.WorkflowSchedule.Type\x12\x33\n\x07one_off\x18\x65 \x01(\x0b\x32 .protos.playbooks.OneOffScheduleH\x00\x12\x36\n\x08interval\x18\x66 \x01(\x0b\x32\".protos.playbooks.IntervalScheduleH\x00\x12.\n\x04\x63ron\x18g \x01(\x0b\x32\x1e.protos.playbooks.CronScheduleH\x00\"8\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07ONE_OFF\x10\x01\x12\x0c\n\x08INTERVAL\x10\x02\x12\x08\n\x04\x43RON\x10\x03\x42\x0b\n\tscheduler\"\xde\x04\n\x12WorkflowEntryPoint\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x37\n\x04type\x18\x02 \x01(\x0e\x32).protos.playbooks.WorkflowEntryPoint.Type\x12\x36\n\x03\x61pi\x18\x65 \x01(\x0b\x32\'.protos.playbooks.ApiWorkflowEntryPointH\x00\x12L\n\x13slack_channel_alert\x18\x66 \x01(\x0b\x32-.protos.playbooks.SlackChannelAlertEntryPointH\x00\x12K\n\x12pagerduty_incident\x18g \x01(\x0b\x32-.protos.playbooks.PagerDutyIncidentEntryPointH\x00\x12G\n\x10zenduty_incident\x18h \x01(\x0b\x32+.protos.playbooks.ZenDutyIncidentEntryPointH\x00\x12\x45\n\x0frootly_incident\x18i \x01(\x0b\x32*.protos.playbooks.RootlyIncidentEntryPointH\x00\"x\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x41PI\x10\x01\x12\x17\n\x13SLACK_CHANNEL_ALERT\x10\x02\x12\x16\n\x12PAGERDUTY_INCIDENT\x10\x03\x12\x14\n\x10ZENDUTY_INCIDENT\x10\x04\x12\x13\n\x0fROOTLY_INCIDENT\x10\x05\x42\x08\n\x06\x63onfig\"\x89\t\n\x0eWorkflowAction\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32%.protos.playbooks.WorkflowAction.Type\x12\x1e\n\x06source\x18\x02 \x01(\x0e\x32\x0e.protos.Source\x12_\n\x17\x61\x63tion_connector_source\x18\x03 \x01(\x0b\x32>.protos.playbooks.WorkflowAction.WorkflowActionConnectorSource\x12\x39\n\x03\x61pi\x18\x65 \x01(\x0b\x32*.protos.playbooks.ApiTriggerWorkflowActionH\x00\x12\x45\n\rslack_message\x18\x66 \x01(\x0b\x32,.protos.playbooks.SlackMessageWorkflowActionH\x00\x12N\n\x12slack_thread_reply\x18g \x01(\x0b\x32\x30.protos.playbooks.SlackThreadReplyWorkflowActionH\x00\x12Y\n\x18ms_teams_message_webhook\x18h \x01(\x0b\x32\x35.protos.playbooks.MSTeamsMessageWebhookWorkflowActionH\x00\x12I\n\x0fpagerduty_notes\x18i \x01(\x0b\x32..protos.playbooks.PagerdutyNotesWorkflowActionH\x00\x12?\n\nsmtp_email\x18j \x01(\x0b\x32).protos.playbooks.SMTPEmailWorkflowActionH\x00\x12\x45\n\rzenduty_notes\x18k \x01(\x0b\x32,.protos.playbooks.ZendutyNotesWorkflowActionH\x00\x12V\n\x16rootly_timeline_events\x18l \x01(\x0b\x32\x34.protos.playbooks.RootlyTimelineEventsWorkflowActionH\x00\x1a\x95\x01\n\x1dWorkflowActionConnectorSource\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x1e\n\x06source\x18\x02 \x01(\x0e\x32\x0e.protos.Source\x12*\n\x04name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xb9\x01\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x41PI\x10\x01\x12\x11\n\rSLACK_MESSAGE\x10\x02\x12\x16\n\x12SLACK_THREAD_REPLY\x10\x03\x12\x1c\n\x18MS_TEAMS_MESSAGE_WEBHOOK\x10\x04\x12\x13\n\x0fPAGERDUTY_NOTES\x10\x05\x12\x0e\n\nSMTP_EMAIL\x10\x06\x12\x11\n\rZENDUTY_NOTES\x10\x07\x12\x1a\n\x16ROOTLY_TIMELINE_EVENTS\x10\x08\x42\x15\n\x13notification_config\"\xec\x05\n\x08Workflow\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x04type\x18\x04 \x01(\x0e\x32\x1f.protos.playbooks.Workflow.Type\x12\x30\n\ncreated_by\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x12\n\ncreated_at\x18\x06 \x01(\x10\x12-\n\tis_active\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\x08schedule\x18\x08 \x01(\x0b\x32\".protos.playbooks.WorkflowSchedule\x12-\n\tplaybooks\x18\t \x03(\x0b\x32\x1a.protos.playbooks.Playbook\x12:\n\x0c\x65ntry_points\x18\n \x03(\x0b\x32$.protos.playbooks.WorkflowEntryPoint\x12\x31\n\x07\x61\x63tions\x18\x0b \x03(\x0b\x32 .protos.playbooks.WorkflowAction\x12\x1b\n\x13last_execution_time\x18\x0c \x01(\x10\x12L\n\x15last_execution_status\x18\r \x01(\x0e\x32-.protos.playbooks.WorkflowExecutionStatusType\x12>\n\rconfiguration\x18\x0e \x01(\x0b\x32\'.protos.playbooks.WorkflowConfiguration\"4\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x11\n\rDYNAMIC_ALERT\x10\x02\"\xb5\x0b\n\x10UpdateWorkflowOp\x12\x31\n\x02op\x18\x01 \x01(\x0e\x32%.protos.playbooks.UpdateWorkflowOp.Op\x12U\n\x14update_workflow_name\x18\x02 \x01(\x0b\x32\x35.protos.playbooks.UpdateWorkflowOp.UpdateWorkflowNameH\x00\x12Y\n\x16update_workflow_status\x18\x03 \x01(\x0b\x32\x37.protos.playbooks.UpdateWorkflowOp.UpdateWorkflowStatusH\x00\x12L\n\x0fupdate_workflow\x18\x04 \x01(\x0b\x32\x31.protos.playbooks.UpdateWorkflowOp.UpdateWorkflowH\x00\x12o\n\"update_workflow_entry_point_status\x18\x05 \x01(\x0b\x32\x41.protos.playbooks.UpdateWorkflowOp.UpdateWorkflowEntryPointStatusH\x00\x12\x66\n\x1dupdate_workflow_action_status\x18\x06 \x01(\x0b\x32=.protos.playbooks.UpdateWorkflowOp.UpdateWorkflowActionStatusH\x00\x12j\n\x1fupdate_workflow_playbook_status\x18\x07 \x01(\x0b\x32?.protos.playbooks.UpdateWorkflowOp.UpdateWorkflowPlaybookStatusH\x00\x1a@\n\x12UpdateWorkflowName\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1a\x45\n\x14UpdateWorkflowStatus\x12-\n\tis_active\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x1a>\n\x0eUpdateWorkflow\x12,\n\x08workflow\x18\x01 \x01(\x0b\x32\x1a.protos.playbooks.Workflow\x1a\x85\x01\n\x1eUpdateWorkflowEntryPointStatus\x12\x34\n\x0e\x65ntry_point_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12-\n\tis_active\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x1a|\n\x1aUpdateWorkflowActionStatus\x12/\n\taction_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12-\n\tis_active\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x1a\x80\x01\n\x1cUpdateWorkflowPlaybookStatus\x12\x31\n\x0bplaybook_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12-\n\tis_active\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\xcc\x01\n\x02Op\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x18\n\x14UPDATE_WORKFLOW_NAME\x10\x01\x12\x1a\n\x16UPDATE_WORKFLOW_STATUS\x10\x02\x12\x13\n\x0fUPDATE_WORKFLOW\x10\x03\x12&\n\"UPDATE_WORKFLOW_ENTRY_POINT_STATUS\x10\x04\x12!\n\x1dUPDATE_WORKFLOW_ACTION_STATUS\x10\x05\x12#\n\x1fUPDATE_WORKFLOW_PLAYBOOK_STATUS\x10\x06\x42\x08\n\x06update\"\x95\x01\n\x14WorkflowExecutionLog\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12?\n\x12playbook_execution\x18\x02 \x01(\x0b\x32#.protos.playbooks.PlaybookExecution\x12\x12\n\ncreated_at\x18\x03 \x01(\x10\"\xb3\x08\n\x11WorkflowExecution\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x35\n\x0fworkflow_run_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x08workflow\x18\x03 \x01(\x0b\x32\x1a.protos.playbooks.Workflow\x12=\n\x06status\x18\x04 \x01(\x0e\x32-.protos.playbooks.WorkflowExecutionStatusType\x12%\n\ntime_range\x18\x05 \x01(\x0b\x32\x11.protos.TimeRange\x12\x12\n\ncreated_at\x18\x06 \x01(\x10\x12\x14\n\x0cscheduled_at\x18\x07 \x01(\x10\x12\x11\n\texpiry_at\x18\x08 \x01(\x10\x12.\n\nkeep_alive\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x12\n\nstarted_at\x18\n \x01(\x10\x12\x1b\n\x13latest_scheduled_at\x18\x0b \x01(\x10\x12\x13\n\x0b\x66inished_at\x18\x0c \x01(\x10\x12\x36\n\x10total_executions\x18\r \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x30\n\ncreated_by\x18\x0e \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12=\n\rworkflow_logs\x18\x0f \x03(\x0b\x32&.protos.playbooks.WorkflowExecutionLog\x12H\n\x17\x65xecution_configuration\x18\x10 \x01(\x0b\x32\'.protos.playbooks.WorkflowConfiguration\x12O\n\x08metadata\x18\x11 \x01(\x0b\x32=.protos.playbooks.WorkflowExecution.WorkflowExecutionMetadata\x1a\xb1\x02\n\x19WorkflowExecutionMetadata\x12P\n\x04type\x18\x01 \x01(\x0e\x32\x42.protos.playbooks.WorkflowExecution.WorkflowExecutionMetadata.Type\x12&\n\x05\x65vent\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12.\n\revent_context\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"j\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rSLACK_MESSAGE\x10\x01\x12\x17\n\x13PAGER_DUTY_INCIDENT\x10\x02\x12\x14\n\x10ZENDUTY_INCIDENT\x10\x03\x12\x13\n\x0fROOTLY_INCIDENT\x10\x04*\xac\x01\n\x1bWorkflowExecutionStatusType\x12\x1b\n\x17UNKNOWN_WORKFLOW_STATUS\x10\x00\x12\x16\n\x12WORKFLOW_SCHEDULED\x10\x01\x12\x14\n\x10WORKFLOW_RUNNING\x10\x02\x12\x15\n\x11WORKFLOW_FINISHED\x10\x03\x12\x13\n\x0fWORKFLOW_FAILED\x10\x04\x12\x16\n\x12WORKFLOW_CANCELLED\x10\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.playbooks.workflow_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WORKFLOWEXECUTIONSTATUSTYPE._serialized_start=7056
  _WORKFLOWEXECUTIONSTATUSTYPE._serialized_end=7228
  _WORKFLOWCONFIGURATION._serialized_start=1260
  _WORKFLOWCONFIGURATION._serialized_end=1531
  _WORKFLOWSCHEDULE._serialized_start=1534
  _WORKFLOWSCHEDULE._serialized_end=1835
  _WORKFLOWSCHEDULE_TYPE._serialized_start=1766
  _WORKFLOWSCHEDULE_TYPE._serialized_end=1822
  _WORKFLOWENTRYPOINT._serialized_start=1838
  _WORKFLOWENTRYPOINT._serialized_end=2444
  _WORKFLOWENTRYPOINT_TYPE._serialized_start=2314
  _WORKFLOWENTRYPOINT_TYPE._serialized_end=2434
  _WORKFLOWACTION._serialized_start=2447
  _WORKFLOWACTION._serialized_end=3608
  _WORKFLOWACTION_WORKFLOWACTIONCONNECTORSOURCE._serialized_start=3248
  _WORKFLOWACTION_WORKFLOWACTIONCONNECTORSOURCE._serialized_end=3397
  _WORKFLOWACTION_TYPE._serialized_start=3400
  _WORKFLOWACTION_TYPE._serialized_end=3585
  _WORKFLOW._serialized_start=3611
  _WORKFLOW._serialized_end=4359
  _WORKFLOW_TYPE._serialized_start=4307
  _WORKFLOW_TYPE._serialized_end=4359
  _UPDATEWORKFLOWOP._serialized_start=4362
  _UPDATEWORKFLOWOP._serialized_end=5823
  _UPDATEWORKFLOWOP_UPDATEWORKFLOWNAME._serialized_start=5014
  _UPDATEWORKFLOWOP_UPDATEWORKFLOWNAME._serialized_end=5078
  _UPDATEWORKFLOWOP_UPDATEWORKFLOWSTATUS._serialized_start=5080
  _UPDATEWORKFLOWOP_UPDATEWORKFLOWSTATUS._serialized_end=5149
  _UPDATEWORKFLOWOP_UPDATEWORKFLOW._serialized_start=5151
  _UPDATEWORKFLOWOP_UPDATEWORKFLOW._serialized_end=5213
  _UPDATEWORKFLOWOP_UPDATEWORKFLOWENTRYPOINTSTATUS._serialized_start=5216
  _UPDATEWORKFLOWOP_UPDATEWORKFLOWENTRYPOINTSTATUS._serialized_end=5349
  _UPDATEWORKFLOWOP_UPDATEWORKFLOWACTIONSTATUS._serialized_start=5351
  _UPDATEWORKFLOWOP_UPDATEWORKFLOWACTIONSTATUS._serialized_end=5475
  _UPDATEWORKFLOWOP_UPDATEWORKFLOWPLAYBOOKSTATUS._serialized_start=5478
  _UPDATEWORKFLOWOP_UPDATEWORKFLOWPLAYBOOKSTATUS._serialized_end=5606
  _UPDATEWORKFLOWOP_OP._serialized_start=5609
  _UPDATEWORKFLOWOP_OP._serialized_end=5813
  _WORKFLOWEXECUTIONLOG._serialized_start=5826
  _WORKFLOWEXECUTIONLOG._serialized_end=5975
  _WORKFLOWEXECUTION._serialized_start=5978
  _WORKFLOWEXECUTION._serialized_end=7053
  _WORKFLOWEXECUTION_WORKFLOWEXECUTIONMETADATA._serialized_start=6748
  _WORKFLOWEXECUTION_WORKFLOWEXECUTIONMETADATA._serialized_end=7053
  _WORKFLOWEXECUTION_WORKFLOWEXECUTIONMETADATA_TYPE._serialized_start=6947
  _WORKFLOWEXECUTION_WORKFLOWEXECUTIONMETADATA_TYPE._serialized_end=7053
# @@protoc_insertion_point(module_scope)
