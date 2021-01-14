# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exabel/api/data/v1/signal_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2

from exabel_data_sdk.stubs.exabel.api.data.v1 import (
    signal_messages_pb2 as exabel_dot_api_dot_data_dot_v1_dot_signal__messages__pb2,
)
from exabel_data_sdk.stubs.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="exabel/api/data/v1/signal_service.proto",
    package="exabel.api.data.v1",
    syntax="proto3",
    serialized_options=b"\n\026com.exabel.api.data.v1B\022SignalServiceProtoP\001",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\'exabel/api/data/v1/signal_service.proto\x12\x12\x65xabel.api.data.v1\x1a(exabel/api/data/v1/signal_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto";\n\x12ListSignalsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t"o\n\x13ListSignalsResponse\x12+\n\x07signals\x18\x01 \x03(\x0b\x32\x1a.exabel.api.data.v1.Signal\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05" \n\x10GetSignalRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"A\n\x13\x43reateSignalRequest\x12*\n\x06signal\x18\x01 \x01(\x0b\x32\x1a.exabel.api.data.v1.Signal"r\n\x13UpdateSignalRequest\x12*\n\x06signal\x18\x01 \x01(\x0b\x32\x1a.exabel.api.data.v1.Signal\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask"#\n\x13\x44\x65leteSignalRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xd5\x04\n\rSignalService\x12s\n\x0bListSignals\x12&.exabel.api.data.v1.ListSignalsRequest\x1a\'.exabel.api.data.v1.ListSignalsResponse"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/v1/signals\x12k\n\tGetSignal\x12$.exabel.api.data.v1.GetSignalRequest\x1a\x1a.exabel.api.data.v1.Signal"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/v1/{name=signals/*}\x12p\n\x0c\x43reateSignal\x12\'.exabel.api.data.v1.CreateSignalRequest\x1a\x1a.exabel.api.data.v1.Signal"\x1b\x82\xd3\xe4\x93\x02\x15"\x0b/v1/signals:\x06signal\x12\x80\x01\n\x0cUpdateSignal\x12\'.exabel.api.data.v1.UpdateSignalRequest\x1a\x1a.exabel.api.data.v1.Signal"+\x82\xd3\xe4\x93\x02%2\x1b/v1/{signal.name=signals/*}:\x06signal\x12m\n\x0c\x44\x65leteSignal\x12\'.exabel.api.data.v1.DeleteSignalRequest\x1a\x16.google.protobuf.Empty"\x1c\x82\xd3\xe4\x93\x02\x16*\x14/v1/{name=signals/*}B.\n\x16\x63om.exabel.api.data.v1B\x12SignalServiceProtoP\x01\x62\x06proto3',
    dependencies=[
        exabel_dot_api_dot_data_dot_v1_dot_signal__messages__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,
    ],
)


_LISTSIGNALSREQUEST = _descriptor.Descriptor(
    name="ListSignalsRequest",
    full_name="exabel.api.data.v1.ListSignalsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="exabel.api.data.v1.ListSignalsRequest.page_size",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_token",
            full_name="exabel.api.data.v1.ListSignalsRequest.page_token",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=198,
    serialized_end=257,
)


_LISTSIGNALSRESPONSE = _descriptor.Descriptor(
    name="ListSignalsResponse",
    full_name="exabel.api.data.v1.ListSignalsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="signals",
            full_name="exabel.api.data.v1.ListSignalsResponse.signals",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="next_page_token",
            full_name="exabel.api.data.v1.ListSignalsResponse.next_page_token",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="total_size",
            full_name="exabel.api.data.v1.ListSignalsResponse.total_size",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=259,
    serialized_end=370,
)


_GETSIGNALREQUEST = _descriptor.Descriptor(
    name="GetSignalRequest",
    full_name="exabel.api.data.v1.GetSignalRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="exabel.api.data.v1.GetSignalRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=372,
    serialized_end=404,
)


_CREATESIGNALREQUEST = _descriptor.Descriptor(
    name="CreateSignalRequest",
    full_name="exabel.api.data.v1.CreateSignalRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="signal",
            full_name="exabel.api.data.v1.CreateSignalRequest.signal",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=406,
    serialized_end=471,
)


_UPDATESIGNALREQUEST = _descriptor.Descriptor(
    name="UpdateSignalRequest",
    full_name="exabel.api.data.v1.UpdateSignalRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="signal",
            full_name="exabel.api.data.v1.UpdateSignalRequest.signal",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="update_mask",
            full_name="exabel.api.data.v1.UpdateSignalRequest.update_mask",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=473,
    serialized_end=587,
)


_DELETESIGNALREQUEST = _descriptor.Descriptor(
    name="DeleteSignalRequest",
    full_name="exabel.api.data.v1.DeleteSignalRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="exabel.api.data.v1.DeleteSignalRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=589,
    serialized_end=624,
)

_LISTSIGNALSRESPONSE.fields_by_name[
    "signals"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_signal__messages__pb2._SIGNAL
_CREATESIGNALREQUEST.fields_by_name[
    "signal"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_signal__messages__pb2._SIGNAL
_UPDATESIGNALREQUEST.fields_by_name[
    "signal"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_signal__messages__pb2._SIGNAL
_UPDATESIGNALREQUEST.fields_by_name[
    "update_mask"
].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name["ListSignalsRequest"] = _LISTSIGNALSREQUEST
DESCRIPTOR.message_types_by_name["ListSignalsResponse"] = _LISTSIGNALSRESPONSE
DESCRIPTOR.message_types_by_name["GetSignalRequest"] = _GETSIGNALREQUEST
DESCRIPTOR.message_types_by_name["CreateSignalRequest"] = _CREATESIGNALREQUEST
DESCRIPTOR.message_types_by_name["UpdateSignalRequest"] = _UPDATESIGNALREQUEST
DESCRIPTOR.message_types_by_name["DeleteSignalRequest"] = _DELETESIGNALREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListSignalsRequest = _reflection.GeneratedProtocolMessageType(
    "ListSignalsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTSIGNALSREQUEST,
        "__module__": "exabel.api.data.v1.signal_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.ListSignalsRequest)
    },
)
_sym_db.RegisterMessage(ListSignalsRequest)

ListSignalsResponse = _reflection.GeneratedProtocolMessageType(
    "ListSignalsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTSIGNALSRESPONSE,
        "__module__": "exabel.api.data.v1.signal_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.ListSignalsResponse)
    },
)
_sym_db.RegisterMessage(ListSignalsResponse)

GetSignalRequest = _reflection.GeneratedProtocolMessageType(
    "GetSignalRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETSIGNALREQUEST,
        "__module__": "exabel.api.data.v1.signal_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.GetSignalRequest)
    },
)
_sym_db.RegisterMessage(GetSignalRequest)

CreateSignalRequest = _reflection.GeneratedProtocolMessageType(
    "CreateSignalRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATESIGNALREQUEST,
        "__module__": "exabel.api.data.v1.signal_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.CreateSignalRequest)
    },
)
_sym_db.RegisterMessage(CreateSignalRequest)

UpdateSignalRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateSignalRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATESIGNALREQUEST,
        "__module__": "exabel.api.data.v1.signal_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.UpdateSignalRequest)
    },
)
_sym_db.RegisterMessage(UpdateSignalRequest)

DeleteSignalRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteSignalRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETESIGNALREQUEST,
        "__module__": "exabel.api.data.v1.signal_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.DeleteSignalRequest)
    },
)
_sym_db.RegisterMessage(DeleteSignalRequest)


DESCRIPTOR._options = None

_SIGNALSERVICE = _descriptor.ServiceDescriptor(
    name="SignalService",
    full_name="exabel.api.data.v1.SignalService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=627,
    serialized_end=1224,
    methods=[
        _descriptor.MethodDescriptor(
            name="ListSignals",
            full_name="exabel.api.data.v1.SignalService.ListSignals",
            index=0,
            containing_service=None,
            input_type=_LISTSIGNALSREQUEST,
            output_type=_LISTSIGNALSRESPONSE,
            serialized_options=b"\202\323\344\223\002\r\022\013/v1/signals",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetSignal",
            full_name="exabel.api.data.v1.SignalService.GetSignal",
            index=1,
            containing_service=None,
            input_type=_GETSIGNALREQUEST,
            output_type=exabel_dot_api_dot_data_dot_v1_dot_signal__messages__pb2._SIGNAL,
            serialized_options=b"\202\323\344\223\002\026\022\024/v1/{name=signals/*}",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="CreateSignal",
            full_name="exabel.api.data.v1.SignalService.CreateSignal",
            index=2,
            containing_service=None,
            input_type=_CREATESIGNALREQUEST,
            output_type=exabel_dot_api_dot_data_dot_v1_dot_signal__messages__pb2._SIGNAL,
            serialized_options=b'\202\323\344\223\002\025"\013/v1/signals:\006signal',
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="UpdateSignal",
            full_name="exabel.api.data.v1.SignalService.UpdateSignal",
            index=3,
            containing_service=None,
            input_type=_UPDATESIGNALREQUEST,
            output_type=exabel_dot_api_dot_data_dot_v1_dot_signal__messages__pb2._SIGNAL,
            serialized_options=b"\202\323\344\223\002%2\033/v1/{signal.name=signals/*}:\006signal",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="DeleteSignal",
            full_name="exabel.api.data.v1.SignalService.DeleteSignal",
            index=4,
            containing_service=None,
            input_type=_DELETESIGNALREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=b"\202\323\344\223\002\026*\024/v1/{name=signals/*}",
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_SIGNALSERVICE)

DESCRIPTOR.services_by_name["SignalService"] = _SIGNALSERVICE

# @@protoc_insertion_point(module_scope)