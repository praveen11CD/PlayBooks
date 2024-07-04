# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/connectors/assets/api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from protos import base_pb2 as protos_dot_base__pb2
from protos.connectors import connector_pb2 as protos_dot_connectors_dot_connector__pb2
from protos.connectors.assets import asset_pb2 as protos_dot_connectors_dot_assets_dot_asset__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"protos/connectors/assets/api.proto\x12\x18protos.connectors.assets\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x11protos/base.proto\x1a!protos/connectors/connector.proto\x1a$protos/connectors/assets/asset.proto\"\xce\x01\n\'GetConnectorsAssetsModelsOptionsRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12&\n\x0e\x63onnector_type\x18\x02 \x01(\x0e\x32\x0e.protos.Source\x12\x32\n\x0c\x63onnector_id\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12+\n\nmodel_type\x18\x04 \x01(\x0e\x32\x17.protos.SourceModelType\"\xf0\x01\n(GetConnectorsAssetsModelsOptionsResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12Y\n\x13\x61sset_model_options\x18\x04 \x03(\x0b\x32<.protos.connectors.assets.AccountConnectorAssetsModelOptions\"\x90\x02\n GetConnectorsAssetsModelsRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x32\n\x0c\x63onnector_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12&\n\x0e\x63onnector_type\x18\x03 \x01(\x0e\x32\x0e.protos.Source\x12%\n\x04type\x18\x04 \x01(\x0e\x32\x17.protos.SourceModelType\x12M\n\x07\x66ilters\x18\x05 \x01(\x0b\x32<.protos.connectors.assets.AccountConnectorAssetsModelFilters\"\xd0\x01\n!GetConnectorsAssetsModelsResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12@\n\x06\x61ssets\x18\x04 \x03(\x0b\x32\x30.protos.connectors.assets.AccountConnectorAssets\"\xe7\x01\n\"GetConnectorsAssetsModelsV2Request\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12/\n\tconnector\x18\x02 \x01(\x0b\x32\x1c.protos.connectors.Connector\x12%\n\x04type\x18\x03 \x01(\x0e\x32\x17.protos.SourceModelType\x12M\n\x07\x66ilters\x18\x04 \x01(\x0b\x32<.protos.connectors.assets.AccountConnectorAssetsModelFilters\"\xd2\x01\n#GetConnectorsAssetsModelsV2Response\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12@\n\x06\x61ssets\x18\x04 \x03(\x0b\x32\x30.protos.connectors.assets.AccountConnectorAssets\"y\n\'GetConnectorsAssetsModelsRefreshRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x32\n\x0c\x63onnector_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\"\x95\x01\n(GetConnectorsAssetsModelsRefreshResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Messageb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.connectors.assets.api_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETCONNECTORSASSETSMODELSOPTIONSREQUEST._serialized_start=189
  _GETCONNECTORSASSETSMODELSOPTIONSREQUEST._serialized_end=395
  _GETCONNECTORSASSETSMODELSOPTIONSRESPONSE._serialized_start=398
  _GETCONNECTORSASSETSMODELSOPTIONSRESPONSE._serialized_end=638
  _GETCONNECTORSASSETSMODELSREQUEST._serialized_start=641
  _GETCONNECTORSASSETSMODELSREQUEST._serialized_end=913
  _GETCONNECTORSASSETSMODELSRESPONSE._serialized_start=916
  _GETCONNECTORSASSETSMODELSRESPONSE._serialized_end=1124
  _GETCONNECTORSASSETSMODELSV2REQUEST._serialized_start=1127
  _GETCONNECTORSASSETSMODELSV2REQUEST._serialized_end=1358
  _GETCONNECTORSASSETSMODELSV2RESPONSE._serialized_start=1361
  _GETCONNECTORSASSETSMODELSV2RESPONSE._serialized_end=1571
  _GETCONNECTORSASSETSMODELSREFRESHREQUEST._serialized_start=1573
  _GETCONNECTORSASSETSMODELSREFRESHREQUEST._serialized_end=1694
  _GETCONNECTORSASSETSMODELSREFRESHRESPONSE._serialized_start=1697
  _GETCONNECTORSASSETSMODELSREFRESHRESPONSE._serialized_end=1846
# @@protoc_insertion_point(module_scope)
