"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
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

class _LiteralType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _LiteralTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_LiteralType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_LT: _LiteralType.ValueType  # 0
    STRING: _LiteralType.ValueType  # 1
    LONG: _LiteralType.ValueType  # 2
    DOUBLE: _LiteralType.ValueType  # 3
    BOOLEAN: _LiteralType.ValueType  # 4
    TIMESTAMP: _LiteralType.ValueType  # 5
    ID: _LiteralType.ValueType  # 6
    STRING_ARRAY: _LiteralType.ValueType  # 7
    LONG_ARRAY: _LiteralType.ValueType  # 8
    DOUBLE_ARRAY: _LiteralType.ValueType  # 9
    BOOLEAN_ARRAY: _LiteralType.ValueType  # 10
    ID_ARRAY: _LiteralType.ValueType  # 12
    NULL_STRING: _LiteralType.ValueType  # 13
    NULL_NUMBER: _LiteralType.ValueType  # 14

class LiteralType(_LiteralType, metaclass=_LiteralTypeEnumTypeWrapper): ...

UNKNOWN_LT: LiteralType.ValueType  # 0
STRING: LiteralType.ValueType  # 1
LONG: LiteralType.ValueType  # 2
DOUBLE: LiteralType.ValueType  # 3
BOOLEAN: LiteralType.ValueType  # 4
TIMESTAMP: LiteralType.ValueType  # 5
ID: LiteralType.ValueType  # 6
STRING_ARRAY: LiteralType.ValueType  # 7
LONG_ARRAY: LiteralType.ValueType  # 8
DOUBLE_ARRAY: LiteralType.ValueType  # 9
BOOLEAN_ARRAY: LiteralType.ValueType  # 10
ID_ARRAY: LiteralType.ValueType  # 12
NULL_STRING: LiteralType.ValueType  # 13
NULL_NUMBER: LiteralType.ValueType  # 14
global___LiteralType = LiteralType

@typing_extensions.final
class IdLiteral(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[IdLiteral._Type.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: IdLiteral._Type.ValueType  # 0
        LONG: IdLiteral._Type.ValueType  # 1
        STRING: IdLiteral._Type.ValueType  # 2

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    UNKNOWN: IdLiteral.Type.ValueType  # 0
    LONG: IdLiteral.Type.ValueType  # 1
    STRING: IdLiteral.Type.ValueType  # 2

    TYPE_FIELD_NUMBER: builtins.int
    ID_COLUMN_FIELD_NUMBER: builtins.int
    LONG_FIELD_NUMBER: builtins.int
    STRING_FIELD_NUMBER: builtins.int
    type: global___IdLiteral.Type.ValueType
    @property
    def id_column(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def long(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    @property
    def string(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        type: global___IdLiteral.Type.ValueType = ...,
        id_column: google.protobuf.wrappers_pb2.StringValue | None = ...,
        long: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        string: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id", "id_column", b"id_column", "long", b"long", "string", b"string"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "id_column", b"id_column", "long", b"long", "string", b"string", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["id", b"id"]) -> typing_extensions.Literal["long", "string"] | None: ...

global___IdLiteral = IdLiteral

@typing_extensions.final
class Literal(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    STRING_FIELD_NUMBER: builtins.int
    LONG_FIELD_NUMBER: builtins.int
    DOUBLE_FIELD_NUMBER: builtins.int
    BOOLEAN_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    STRING_ARRAY_FIELD_NUMBER: builtins.int
    LONG_ARRAY_FIELD_NUMBER: builtins.int
    DOUBLE_ARRAY_FIELD_NUMBER: builtins.int
    BYTES_ARRAY_FIELD_NUMBER: builtins.int
    BOOLEAN_ARRAY_FIELD_NUMBER: builtins.int
    ID_ARRAY_FIELD_NUMBER: builtins.int
    type: global___LiteralType.ValueType
    """Referenced from: https://github.com/hypertrace/entity-service/blob/main/entity-service-api/src/main/proto/org/hypertrace/entity/query/service/v1/value.proto"""
    @property
    def string(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def long(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def double(self) -> google.protobuf.wrappers_pb2.DoubleValue: ...
    @property
    def boolean(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    timestamp: builtins.int
    @property
    def id(self) -> global___IdLiteral: ...
    @property
    def string_array(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def long_array(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def double_array(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    @property
    def bytes_array(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    @property
    def boolean_array(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bool]: ...
    @property
    def id_array(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___IdLiteral]: ...
    def __init__(
        self,
        *,
        type: global___LiteralType.ValueType = ...,
        string: google.protobuf.wrappers_pb2.StringValue | None = ...,
        long: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        double: google.protobuf.wrappers_pb2.DoubleValue | None = ...,
        boolean: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        timestamp: builtins.int = ...,
        id: global___IdLiteral | None = ...,
        string_array: collections.abc.Iterable[builtins.str] | None = ...,
        long_array: collections.abc.Iterable[builtins.int] | None = ...,
        double_array: collections.abc.Iterable[builtins.float] | None = ...,
        bytes_array: collections.abc.Iterable[builtins.bytes] | None = ...,
        boolean_array: collections.abc.Iterable[builtins.bool] | None = ...,
        id_array: collections.abc.Iterable[global___IdLiteral] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["boolean", b"boolean", "double", b"double", "id", b"id", "long", b"long", "string", b"string"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["boolean", b"boolean", "boolean_array", b"boolean_array", "bytes_array", b"bytes_array", "double", b"double", "double_array", b"double_array", "id", b"id", "id_array", b"id_array", "long", b"long", "long_array", b"long_array", "string", b"string", "string_array", b"string_array", "timestamp", b"timestamp", "type", b"type"]) -> None: ...

global___Literal = Literal

@typing_extensions.final
class LiteralTypeDescription(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LITERAL_TYPE_FIELD_NUMBER: builtins.int
    LABEL_FIELD_NUMBER: builtins.int
    literal_type: global___LiteralType.ValueType
    label: builtins.str
    def __init__(
        self,
        *,
        literal_type: global___LiteralType.ValueType = ...,
        label: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["label", b"label", "literal_type", b"literal_type"]) -> None: ...

global___LiteralTypeDescription = LiteralTypeDescription
