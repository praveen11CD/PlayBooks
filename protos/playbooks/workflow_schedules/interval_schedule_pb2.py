# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/playbooks/workflow_schedules/interval_schedule.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from protos import base_pb2 as protos_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;protos/playbooks/workflow_schedules/interval_schedule.proto\x12\x10protos.playbooks\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x11protos/base.proto\"\x88\x01\n\x10IntervalSchedule\x12\x39\n\x13\x64uration_in_seconds\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x39\n\x13interval_in_seconds\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64Valueb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.playbooks.workflow_schedules.interval_schedule_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INTERVALSCHEDULE._serialized_start=133
  _INTERVALSCHEDULE._serialized_end=269
# @@protoc_insertion_point(module_scope)
