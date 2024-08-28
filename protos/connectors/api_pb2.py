# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/connectors/api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from protos.connectors import connector_pb2 as protos_dot_connectors_dot_connector__pb2
from protos.connectors import alert_ops_pb2 as protos_dot_connectors_dot_alert__ops__pb2
from protos import base_pb2 as protos_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bprotos/connectors/api.proto\x12\x11protos.connectors\x1a\x1egoogle/protobuf/wrappers.proto\x1a!protos/connectors/connector.proto\x1a!protos/connectors/alert_ops.proto\x1a\x11protos/base.proto\"\x82\x01\n\x16\x43reateConnectorRequest\x12/\n\tconnector\x18\x01 \x01(\x0b\x32\x1c.protos.connectors.Connector\x12\x37\n\x0e\x63onnector_keys\x18\x02 \x03(\x0b\x32\x1f.protos.connectors.ConnectorKey\"h\n\x17\x43reateConnectorResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\"I\n\x13GetConnectorRequest\x12\x32\n\x0c\x63onnector_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\"\x96\x01\n\x14GetConnectorResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\x12/\n\tconnector\x18\x03 \x01(\x0b\x32\x1c.protos.connectors.Connector\"B\n\x18GetConnectorsListRequest\x12&\n\x0e\x63onnector_type\x18\x01 \x01(\x0e\x32\x0e.protos.Source\"\x92\x02\n\x19GetConnectorsListResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\x12\x38\n\x12request_connectors\x18\x03 \x03(\x0b\x32\x1c.protos.connectors.Connector\x12:\n\x14\x61vailable_connectors\x18\x04 \x03(\x0b\x32\x1c.protos.connectors.Connector\x12\x30\n\nconnectors\x18\x05 \x03(\x0b\x32\x1c.protos.connectors.Connector\"\x90\x01\n\x16UpdateConnectorRequest\x12\x32\n\x0c\x63onnector_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x42\n\x14update_connector_ops\x18\x02 \x03(\x0b\x32$.protos.connectors.UpdateConnectorOp\"h\n\x17UpdateConnectorResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\"H\n\x1eGetConnectorKeysOptionsRequest\x12&\n\x0e\x63onnector_type\x18\x01 \x01(\x0e\x32\x0e.protos.Source\"\xe1\x01\n\x1fGetConnectorKeysOptionsResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\x12/\n\tconnector\x18\x03 \x01(\x0b\x32\x1c.protos.connectors.Connector\x12>\n\x15\x63onnector_key_options\x18\x04 \x03(\x0b\x32\x1f.protos.connectors.ConnectorKey\"u\n\x17GetConnectorKeysRequest\x12\x32\n\x0c\x63onnector_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12&\n\x0e\x63onnector_type\x18\x02 \x01(\x0e\x32\x0e.protos.Source\"\xd3\x01\n\x18GetConnectorKeysResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\x12/\n\tconnector\x18\x03 \x01(\x0b\x32\x1c.protos.connectors.Connector\x12\x37\n\x0e\x63onnector_keys\x18\x04 \x03(\x0b\x32\x1f.protos.connectors.ConnectorKey\"F\n(GetConnectorPlaybookSourceOptionsRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\"\xcc\x01\n)GetConnectorPlaybookSourceOptionsResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12V\n\x19\x61\x63tive_account_connectors\x18\x03 \x03(\x0b\x32\x33.protos.connectors.AccountActiveConnectorModelTypes\"\xbe\x02\n\"GetSlackAlertTriggerOptionsRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12k\n\x17\x63onnector_type_requests\x18\x02 \x03(\x0b\x32J.protos.connectors.GetSlackAlertTriggerOptionsRequest.ConnectorTypeRequest\x1a\x8e\x01\n\x14\x43onnectorTypeRequest\x12&\n\x0e\x63onnector_type\x18\x01 \x01(\x0e\x32\x0e.protos.Source\x12\x17\n\x0f\x66ilter_channels\x18\x02 \x03(\t\x12\x1a\n\x12\x66ilter_alert_types\x18\x03 \x03(\t\x12\x19\n\x11\x66ilter_alert_tags\x18\x04 \x03(\t\"n\n#GetSlackAlertTriggerOptionsResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x11\x61lert_ops_options\x18\x02 \x01(\x0b\x32\x10.AlertOpsOptions\"\xb2\x02\n\x15GetSlackAlertsRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x36\n\x12use_db_source_tags\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0cworkspace_id\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x30\n\nchannel_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nalert_type\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07pattern\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"W\n\x16GetSlackAlertsResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12!\n\x0cslack_alerts\x18\x02 \x03(\x0b\x32\x0b.SlackAlert\"M\n\x1aGetSlackAppManifestRequest\x12/\n\thost_name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xa0\x01\n\x1bGetSlackAppManifestResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\x12\x32\n\x0c\x61pp_manifest\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"n\n\x1cGetConnectedPlaybooksRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x32\n\x0c\x63onnector_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\"\xd6\x02\n\x1dGetConnectedPlaybooksResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12V\n\x13\x63onnected_playbooks\x18\x04 \x03(\x0b\x32\x39.protos.connectors.GetConnectedPlaybooksResponse.Playbook\x1ar\n\x08Playbook\x12\x31\n\x0bplaybook_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x33\n\rplaybook_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x1c\n\x1aGetPagerDutyWebhookRequest\"\x1d\n\x1bGetPagerDutyWebhookResponse\"\x19\n\x17GetRootlyWebhookRequest\"\x1a\n\x18GetRootlyWebhookResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.connectors.api_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATECONNECTORREQUEST._serialized_start=172
  _CREATECONNECTORREQUEST._serialized_end=302
  _CREATECONNECTORRESPONSE._serialized_start=304
  _CREATECONNECTORRESPONSE._serialized_end=408
  _GETCONNECTORREQUEST._serialized_start=410
  _GETCONNECTORREQUEST._serialized_end=483
  _GETCONNECTORRESPONSE._serialized_start=486
  _GETCONNECTORRESPONSE._serialized_end=636
  _GETCONNECTORSLISTREQUEST._serialized_start=638
  _GETCONNECTORSLISTREQUEST._serialized_end=704
  _GETCONNECTORSLISTRESPONSE._serialized_start=707
  _GETCONNECTORSLISTRESPONSE._serialized_end=981
  _UPDATECONNECTORREQUEST._serialized_start=984
  _UPDATECONNECTORREQUEST._serialized_end=1128
  _UPDATECONNECTORRESPONSE._serialized_start=1130
  _UPDATECONNECTORRESPONSE._serialized_end=1234
  _GETCONNECTORKEYSOPTIONSREQUEST._serialized_start=1236
  _GETCONNECTORKEYSOPTIONSREQUEST._serialized_end=1308
  _GETCONNECTORKEYSOPTIONSRESPONSE._serialized_start=1311
  _GETCONNECTORKEYSOPTIONSRESPONSE._serialized_end=1536
  _GETCONNECTORKEYSREQUEST._serialized_start=1538
  _GETCONNECTORKEYSREQUEST._serialized_end=1655
  _GETCONNECTORKEYSRESPONSE._serialized_start=1658
  _GETCONNECTORKEYSRESPONSE._serialized_end=1869
  _GETCONNECTORPLAYBOOKSOURCEOPTIONSREQUEST._serialized_start=1871
  _GETCONNECTORPLAYBOOKSOURCEOPTIONSREQUEST._serialized_end=1941
  _GETCONNECTORPLAYBOOKSOURCEOPTIONSRESPONSE._serialized_start=1944
  _GETCONNECTORPLAYBOOKSOURCEOPTIONSRESPONSE._serialized_end=2148
  _GETSLACKALERTTRIGGEROPTIONSREQUEST._serialized_start=2151
  _GETSLACKALERTTRIGGEROPTIONSREQUEST._serialized_end=2469
  _GETSLACKALERTTRIGGEROPTIONSREQUEST_CONNECTORTYPEREQUEST._serialized_start=2327
  _GETSLACKALERTTRIGGEROPTIONSREQUEST_CONNECTORTYPEREQUEST._serialized_end=2469
  _GETSLACKALERTTRIGGEROPTIONSRESPONSE._serialized_start=2471
  _GETSLACKALERTTRIGGEROPTIONSRESPONSE._serialized_end=2581
  _GETSLACKALERTSREQUEST._serialized_start=2584
  _GETSLACKALERTSREQUEST._serialized_end=2890
  _GETSLACKALERTSRESPONSE._serialized_start=2892
  _GETSLACKALERTSRESPONSE._serialized_end=2979
  _GETSLACKAPPMANIFESTREQUEST._serialized_start=2981
  _GETSLACKAPPMANIFESTREQUEST._serialized_end=3058
  _GETSLACKAPPMANIFESTRESPONSE._serialized_start=3061
  _GETSLACKAPPMANIFESTRESPONSE._serialized_end=3221
  _GETCONNECTEDPLAYBOOKSREQUEST._serialized_start=3223
  _GETCONNECTEDPLAYBOOKSREQUEST._serialized_end=3333
  _GETCONNECTEDPLAYBOOKSRESPONSE._serialized_start=3336
  _GETCONNECTEDPLAYBOOKSRESPONSE._serialized_end=3678
  _GETCONNECTEDPLAYBOOKSRESPONSE_PLAYBOOK._serialized_start=3564
  _GETCONNECTEDPLAYBOOKSRESPONSE_PLAYBOOK._serialized_end=3678
  _GETPAGERDUTYWEBHOOKREQUEST._serialized_start=3680
  _GETPAGERDUTYWEBHOOKREQUEST._serialized_end=3708
  _GETPAGERDUTYWEBHOOKRESPONSE._serialized_start=3710
  _GETPAGERDUTYWEBHOOKRESPONSE._serialized_end=3739
  _GETROOTLYWEBHOOKREQUEST._serialized_start=3741
  _GETROOTLYWEBHOOKREQUEST._serialized_end=3766
  _GETROOTLYWEBHOOKRESPONSE._serialized_start=3768
  _GETROOTLYWEBHOOKRESPONSE._serialized_end=3794
# @@protoc_insertion_point(module_scope)
