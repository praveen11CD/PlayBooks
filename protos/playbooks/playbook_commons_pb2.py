# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/playbooks/playbook_commons.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import base_pb2 as protos_dot_base__pb2
from protos import ui_definition_pb2 as protos_dot_ui__definition__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'protos/playbooks/playbook_commons.proto\x12\x10protos.playbooks\x1a\x11protos/base.proto\x1a\x1aprotos/ui_definition.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/protobuf/struct.proto\"e\n\x0c\x45xternalLink\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x03url\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"i\n\x0eLabelValuePair\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x8b\x04\n\x10TimeseriesResult\x12\x31\n\x0bmetric_name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11metric_expression\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12]\n\x19labeled_metric_timeseries\x18\x03 \x03(\x0b\x32:.protos.playbooks.TimeseriesResult.LabeledMetricTimeseries\x1a\xab\x02\n\x17LabeledMetricTimeseries\x12=\n\x13metric_label_values\x18\x01 \x03(\x0b\x32 .protos.playbooks.LabelValuePair\x12*\n\x04unit\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12X\n\ndatapoints\x18\x03 \x03(\x0b\x32\x44.protos.playbooks.TimeseriesResult.LabeledMetricTimeseries.Datapoint\x1aK\n\tDatapoint\x12\x11\n\ttimestamp\x18\x01 \x01(\x10\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\"\xdf\x03\n\x0bTableResult\x12/\n\traw_query\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0btotal_count\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12+\n\x05limit\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12,\n\x06offset\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x34\n\x04rows\x18\x05 \x03(\x0b\x32&.protos.playbooks.TableResult.TableRow\x1a\x92\x01\n\x0bTableColumn\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04type\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05value\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1a\x46\n\x08TableRow\x12:\n\x07\x63olumns\x18\x01 \x03(\x0b\x32).protos.playbooks.TableResult.TableColumn\"\xe9\x02\n\x11\x41piResponseResult\x12\x34\n\x0erequest_method\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0brequest_url\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0fresponse_status\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x31\n\x10response_headers\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12.\n\rresponse_body\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12&\n\x05\x65rror\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08metadata\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xd9\x01\n\x17\x42\x61shCommandOutputResult\x12P\n\x0f\x63ommand_outputs\x18\x01 \x03(\x0b\x32\x37.protos.playbooks.BashCommandOutputResult.CommandOutput\x1al\n\rCommandOutput\x12-\n\x07\x63ommand\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06output\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\":\n\nTextResult\x12,\n\x06output\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xab\x04\n\x12PlaybookTaskResult\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x04type\x18\x02 \x01(\x0e\x32(.protos.playbooks.PlaybookTaskResultType\x12\x1e\n\x06source\x18\x03 \x01(\x0e\x32\x0e.protos.Source\x12\x38\n\x17task_local_variable_set\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x38\n\ntimeseries\x18\x65 \x01(\x0b\x32\".protos.playbooks.TimeseriesResultH\x00\x12.\n\x05table\x18\x66 \x01(\x0b\x32\x1d.protos.playbooks.TableResultH\x00\x12;\n\x0c\x61pi_response\x18g \x01(\x0b\x32#.protos.playbooks.ApiResponseResultH\x00\x12H\n\x13\x62\x61sh_command_output\x18h \x01(\x0b\x32).protos.playbooks.BashCommandOutputResultH\x00\x12,\n\x04text\x18i \x01(\x0b\x32\x1c.protos.playbooks.TextResultH\x00\x12-\n\x04logs\x18j \x01(\x0b\x32\x1d.protos.playbooks.TableResultH\x00\x42\x08\n\x06result\"\x87\x07\n\x15PlaybookSourceOptions\x12\x1e\n\x06source\x18\x01 \x01(\x0e\x32\x0e.protos.Source\x12\x32\n\x0c\x64isplay_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12[\n\x1bsupported_task_type_options\x18\x03 \x03(\x0b\x32\x36.protos.playbooks.PlaybookSourceOptions.TaskTypeOption\x12R\n\x11\x63onnector_options\x18\x04 \x03(\x0b\x32\x37.protos.playbooks.PlaybookSourceOptions.ConnectorOption\x1ay\n\x0f\x43onnectorOption\x12\x32\n\x0c\x63onnector_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x32\n\x0c\x64isplay_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1a\xed\x03\n\x0eTaskTypeOption\x12\x32\n\x0c\x64isplay_name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\ttask_type\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x63\x61tegory\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12h\n\x15supported_model_types\x18\x04 \x03(\x0b\x32I.protos.playbooks.PlaybookSourceOptions.TaskTypeOption.SourceModelTypeMap\x12=\n\x0bresult_type\x18\x05 \x01(\x0e\x32(.protos.playbooks.PlaybookTaskResultType\x12&\n\x0b\x66orm_fields\x18\x06 \x03(\x0b\x32\x11.protos.FormField\x1au\n\x12SourceModelTypeMap\x12+\n\nmodel_type\x18\x01 \x01(\x0e\x32\x17.protos.SourceModelType\x12\x32\n\x0c\x64isplay_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue*e\n\x1bPlaybookExecutionStatusType\x12\x12\n\x0eUNKNOWN_STATUS\x10\x00\x12\x0b\n\x07\x43REATED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0c\n\x08\x46INISHED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04*\x7f\n\x16PlaybookTaskResultType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nTIMESERIES\x10\x01\x12\t\n\x05TABLE\x10\x02\x12\x10\n\x0c\x41PI_RESPONSE\x10\x03\x12\x17\n\x13\x42\x41SH_COMMAND_OUTPUT\x10\x04\x12\x08\n\x04TEXT\x10\x05\x12\x08\n\x04LOGS\x10\x06\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.playbooks.playbook_commons_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYBOOKEXECUTIONSTATUSTYPE._serialized_start=3496
  _PLAYBOOKEXECUTIONSTATUSTYPE._serialized_end=3597
  _PLAYBOOKTASKRESULTTYPE._serialized_start=3599
  _PLAYBOOKTASKRESULTTYPE._serialized_end=3726
  _EXTERNALLINK._serialized_start=170
  _EXTERNALLINK._serialized_end=271
  _LABELVALUEPAIR._serialized_start=273
  _LABELVALUEPAIR._serialized_end=378
  _TIMESERIESRESULT._serialized_start=381
  _TIMESERIESRESULT._serialized_end=904
  _TIMESERIESRESULT_LABELEDMETRICTIMESERIES._serialized_start=605
  _TIMESERIESRESULT_LABELEDMETRICTIMESERIES._serialized_end=904
  _TIMESERIESRESULT_LABELEDMETRICTIMESERIES_DATAPOINT._serialized_start=829
  _TIMESERIESRESULT_LABELEDMETRICTIMESERIES_DATAPOINT._serialized_end=904
  _TABLERESULT._serialized_start=907
  _TABLERESULT._serialized_end=1386
  _TABLERESULT_TABLECOLUMN._serialized_start=1168
  _TABLERESULT_TABLECOLUMN._serialized_end=1314
  _TABLERESULT_TABLEROW._serialized_start=1316
  _TABLERESULT_TABLEROW._serialized_end=1386
  _APIRESPONSERESULT._serialized_start=1389
  _APIRESPONSERESULT._serialized_end=1750
  _BASHCOMMANDOUTPUTRESULT._serialized_start=1753
  _BASHCOMMANDOUTPUTRESULT._serialized_end=1970
  _BASHCOMMANDOUTPUTRESULT_COMMANDOUTPUT._serialized_start=1862
  _BASHCOMMANDOUTPUTRESULT_COMMANDOUTPUT._serialized_end=1970
  _TEXTRESULT._serialized_start=1972
  _TEXTRESULT._serialized_end=2030
  _PLAYBOOKTASKRESULT._serialized_start=2033
  _PLAYBOOKTASKRESULT._serialized_end=2588
  _PLAYBOOKSOURCEOPTIONS._serialized_start=2591
  _PLAYBOOKSOURCEOPTIONS._serialized_end=3494
  _PLAYBOOKSOURCEOPTIONS_CONNECTOROPTION._serialized_start=2877
  _PLAYBOOKSOURCEOPTIONS_CONNECTOROPTION._serialized_end=2998
  _PLAYBOOKSOURCEOPTIONS_TASKTYPEOPTION._serialized_start=3001
  _PLAYBOOKSOURCEOPTIONS_TASKTYPEOPTION._serialized_end=3494
  _PLAYBOOKSOURCEOPTIONS_TASKTYPEOPTION_SOURCEMODELTYPEMAP._serialized_start=3377
  _PLAYBOOKSOURCEOPTIONS_TASKTYPEOPTION_SOURCEMODELTYPEMAP._serialized_end=3494
# @@protoc_insertion_point(module_scope)
