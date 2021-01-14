# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from typing import Iterable as typing___Iterable
from typing import Optional as typing___Optional
from typing import Text as typing___Text

from google.protobuf.descriptor import Descriptor as google___protobuf___descriptor___Descriptor
from google.protobuf.descriptor import (
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.timestamp_pb2 import Timestamp as google___protobuf___timestamp_pb2___Timestamp
from google.protobuf.wrappers_pb2 import (
    DoubleValue as google___protobuf___wrappers_pb2___DoubleValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from exabel_data_sdk.stubs.exabel.api.time.time_range_pb2 import (
    TimeRange as exabel___api___time___time_range_pb2___TimeRange,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class TimeSeries(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...
    read_only: builtin___bool = ...
    @property
    def points(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___TimeSeriesPoint
    ]: ...
    def __init__(
        self,
        *,
        name: typing___Optional[typing___Text] = None,
        points: typing___Optional[typing___Iterable[type___TimeSeriesPoint]] = None,
        read_only: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "name", b"name", "points", b"points", "read_only", b"read_only"
        ],
    ) -> None: ...

type___TimeSeries = TimeSeries

class TimeSeriesPoint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def time(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
    @property
    def value(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    def __init__(
        self,
        *,
        time: typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        value: typing___Optional[google___protobuf___wrappers_pb2___DoubleValue] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal["time", b"time", "value", b"value"],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal["time", b"time", "value", b"value"],
    ) -> None: ...

type___TimeSeriesPoint = TimeSeriesPoint

class TimeSeriesView(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def time_range(self) -> exabel___api___time___time_range_pb2___TimeRange: ...
    def __init__(
        self,
        *,
        time_range: typing___Optional[exabel___api___time___time_range_pb2___TimeRange] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["time_range", b"time_range"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["time_range", b"time_range"]
    ) -> None: ...

type___TimeSeriesView = TimeSeriesView