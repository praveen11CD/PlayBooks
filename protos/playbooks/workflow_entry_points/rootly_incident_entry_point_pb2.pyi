"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class RootlyIncidentEntryPoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_NAME_FIELD_NUMBER: builtins.int
    INCIDENT_TITLE_FIELD_NUMBER: builtins.int
    SERVICE_ID_FIELD_NUMBER: builtins.int
    INCIDENT_ID_FIELD_NUMBER: builtins.int
    @property
    def service_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def incident_title(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def service_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def incident_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        service_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        incident_title: google.protobuf.wrappers_pb2.StringValue | None = ...,
        service_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        incident_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["incident_id", b"incident_id", "incident_title", b"incident_title", "service_id", b"service_id", "service_name", b"service_name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["incident_id", b"incident_id", "incident_title", b"incident_title", "service_id", b"service_id", "service_name", b"service_name"]) -> None: ...

global___RootlyIncidentEntryPoint = RootlyIncidentEntryPoint
