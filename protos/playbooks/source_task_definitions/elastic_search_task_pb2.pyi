"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ElasticSearch(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _TaskType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TaskTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ElasticSearch._TaskType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: ElasticSearch._TaskType.ValueType  # 0
        QUERY_INDEX: ElasticSearch._TaskType.ValueType  # 1

    class TaskType(_TaskType, metaclass=_TaskTypeEnumTypeWrapper): ...
    UNKNOWN: ElasticSearch.TaskType.ValueType  # 0
    QUERY_INDEX: ElasticSearch.TaskType.ValueType  # 1

    @typing_extensions.final
    class QueryIndex(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        INDEX_FIELD_NUMBER: builtins.int
        QUERY_FIELD_NUMBER: builtins.int
        @property
        def index(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def query(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        def __init__(
            self,
            *,
            index: google.protobuf.wrappers_pb2.StringValue | None = ...,
            query: google.protobuf.wrappers_pb2.StringValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["index", b"index", "query", b"query"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["index", b"index", "query", b"query"]) -> None: ...

    TYPE_FIELD_NUMBER: builtins.int
    QUERY_INDEX_FIELD_NUMBER: builtins.int
    type: global___ElasticSearch.TaskType.ValueType
    @property
    def query_index(self) -> global___ElasticSearch.QueryIndex: ...
    def __init__(
        self,
        *,
        type: global___ElasticSearch.TaskType.ValueType = ...,
        query_index: global___ElasticSearch.QueryIndex | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["query_index", b"query_index", "task", b"task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["query_index", b"query_index", "task", b"task", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["task", b"task"]) -> typing_extensions.Literal["query_index"] | None: ...

global___ElasticSearch = ElasticSearch
