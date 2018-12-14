# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: muscle_manager_protocol.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='muscle_manager_protocol.proto',
  package='muscle_manager_protocol',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dmuscle_manager_protocol.proto\x12\x17muscle_manager_protocol\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc5\x01\n\nLogMessage\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\x12\x33\n\x08operator\x18\x02 \x01(\x0e\x32!.muscle_manager_protocol.Operator\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x05level\x18\x04 \x01(\x0e\x32!.muscle_manager_protocol.LogLevel\x12\x0c\n\x04text\x18\x05 \x01(\t\"\x0b\n\tLogResult\"I\n\x04Port\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x33\n\x08operator\x18\x02 \x01(\x0e\x32!.muscle_manager_protocol.Operator\"u\n\x13RegistrationRequest\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\x19\n\x11network_locations\x18\x02 \x03(\t\x12,\n\x05ports\x18\x03 \x03(\x0b\x32\x1d.muscle_manager_protocol.Port\"b\n\x12RegistrationResult\x12\x35\n\x06status\x18\x01 \x01(\x0e\x32%.muscle_manager_protocol.ResultStatus\x12\x15\n\rerror_message\x18\x02 \x01(\t*]\n\x0cResultStatus\x12\x19\n\x15RESULT_STATUS_SUCCESS\x10\x00\x12\x17\n\x13RESULT_STATUS_ERROR\x10\x01\x12\x19\n\x15RESULT_STATUS_PENDING\x10\x02*\x88\x01\n\x08Operator\x12\x11\n\rOPERATOR_NONE\x10\x00\x12\x13\n\x0fOPERATOR_F_INIT\x10\x01\x12\x10\n\x0cOPERATOR_O_I\x10\x02\x12\x0e\n\nOPERATOR_S\x10\x03\x12\x0e\n\nOPERATOR_B\x10\x04\x12\x10\n\x0cOPERATOR_O_F\x10\x05\x12\x10\n\x0cOPERATOR_MAP\x10\x06*\x8e\x01\n\x08LogLevel\x12\x13\n\x0fLOG_LEVEL_DEBUG\x10\x00\x12\x12\n\x0eLOG_LEVEL_INFO\x10\x01\x12\x15\n\x11LOG_LEVEL_PROFILE\x10\x02\x12\x15\n\x11LOG_LEVEL_WARNING\x10\x03\x12\x13\n\x0fLOG_LEVEL_ERROR\x10\x04\x12\x16\n\x12LOG_LEVEL_CRITICAL\x10\x05\x32\xdb\x01\n\rMuscleManager\x12[\n\x10SubmitLogMessage\x12#.muscle_manager_protocol.LogMessage\x1a\".muscle_manager_protocol.LogResult\x12m\n\x10RegisterInstance\x12,.muscle_manager_protocol.RegistrationRequest\x1a+.muscle_manager_protocol.RegistrationResultb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_RESULTSTATUS = _descriptor.EnumDescriptor(
  name='ResultStatus',
  full_name='muscle_manager_protocol.ResultStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_STATUS_SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_STATUS_ERROR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_STATUS_PENDING', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=598,
  serialized_end=691,
)
_sym_db.RegisterEnumDescriptor(_RESULTSTATUS)

ResultStatus = enum_type_wrapper.EnumTypeWrapper(_RESULTSTATUS)
_OPERATOR = _descriptor.EnumDescriptor(
  name='Operator',
  full_name='muscle_manager_protocol.Operator',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_F_INIT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_O_I', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_S', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_B', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_O_F', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_MAP', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=694,
  serialized_end=830,
)
_sym_db.RegisterEnumDescriptor(_OPERATOR)

Operator = enum_type_wrapper.EnumTypeWrapper(_OPERATOR)
_LOGLEVEL = _descriptor.EnumDescriptor(
  name='LogLevel',
  full_name='muscle_manager_protocol.LogLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LOG_LEVEL_DEBUG', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOG_LEVEL_INFO', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOG_LEVEL_PROFILE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOG_LEVEL_WARNING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOG_LEVEL_ERROR', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOG_LEVEL_CRITICAL', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=833,
  serialized_end=975,
)
_sym_db.RegisterEnumDescriptor(_LOGLEVEL)

LogLevel = enum_type_wrapper.EnumTypeWrapper(_LOGLEVEL)
RESULT_STATUS_SUCCESS = 0
RESULT_STATUS_ERROR = 1
RESULT_STATUS_PENDING = 2
OPERATOR_NONE = 0
OPERATOR_F_INIT = 1
OPERATOR_O_I = 2
OPERATOR_S = 3
OPERATOR_B = 4
OPERATOR_O_F = 5
OPERATOR_MAP = 6
LOG_LEVEL_DEBUG = 0
LOG_LEVEL_INFO = 1
LOG_LEVEL_PROFILE = 2
LOG_LEVEL_WARNING = 3
LOG_LEVEL_ERROR = 4
LOG_LEVEL_CRITICAL = 5



_LOGMESSAGE = _descriptor.Descriptor(
  name='LogMessage',
  full_name='muscle_manager_protocol.LogMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='muscle_manager_protocol.LogMessage.instance_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operator', full_name='muscle_manager_protocol.LogMessage.operator', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='muscle_manager_protocol.LogMessage.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='muscle_manager_protocol.LogMessage.level', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='muscle_manager_protocol.LogMessage.text', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=289,
)


_LOGRESULT = _descriptor.Descriptor(
  name='LogResult',
  full_name='muscle_manager_protocol.LogResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=302,
)


_PORT = _descriptor.Descriptor(
  name='Port',
  full_name='muscle_manager_protocol.Port',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='muscle_manager_protocol.Port.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operator', full_name='muscle_manager_protocol.Port.operator', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=304,
  serialized_end=377,
)


_REGISTRATIONREQUEST = _descriptor.Descriptor(
  name='RegistrationRequest',
  full_name='muscle_manager_protocol.RegistrationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='muscle_manager_protocol.RegistrationRequest.instance_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_locations', full_name='muscle_manager_protocol.RegistrationRequest.network_locations', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ports', full_name='muscle_manager_protocol.RegistrationRequest.ports', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=379,
  serialized_end=496,
)


_REGISTRATIONRESULT = _descriptor.Descriptor(
  name='RegistrationResult',
  full_name='muscle_manager_protocol.RegistrationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='muscle_manager_protocol.RegistrationResult.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='muscle_manager_protocol.RegistrationResult.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=498,
  serialized_end=596,
)

_LOGMESSAGE.fields_by_name['operator'].enum_type = _OPERATOR
_LOGMESSAGE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOGMESSAGE.fields_by_name['level'].enum_type = _LOGLEVEL
_PORT.fields_by_name['operator'].enum_type = _OPERATOR
_REGISTRATIONREQUEST.fields_by_name['ports'].message_type = _PORT
_REGISTRATIONRESULT.fields_by_name['status'].enum_type = _RESULTSTATUS
DESCRIPTOR.message_types_by_name['LogMessage'] = _LOGMESSAGE
DESCRIPTOR.message_types_by_name['LogResult'] = _LOGRESULT
DESCRIPTOR.message_types_by_name['Port'] = _PORT
DESCRIPTOR.message_types_by_name['RegistrationRequest'] = _REGISTRATIONREQUEST
DESCRIPTOR.message_types_by_name['RegistrationResult'] = _REGISTRATIONRESULT
DESCRIPTOR.enum_types_by_name['ResultStatus'] = _RESULTSTATUS
DESCRIPTOR.enum_types_by_name['Operator'] = _OPERATOR
DESCRIPTOR.enum_types_by_name['LogLevel'] = _LOGLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogMessage = _reflection.GeneratedProtocolMessageType('LogMessage', (_message.Message,), dict(
  DESCRIPTOR = _LOGMESSAGE,
  __module__ = 'muscle_manager_protocol_pb2'
  # @@protoc_insertion_point(class_scope:muscle_manager_protocol.LogMessage)
  ))
_sym_db.RegisterMessage(LogMessage)

LogResult = _reflection.GeneratedProtocolMessageType('LogResult', (_message.Message,), dict(
  DESCRIPTOR = _LOGRESULT,
  __module__ = 'muscle_manager_protocol_pb2'
  # @@protoc_insertion_point(class_scope:muscle_manager_protocol.LogResult)
  ))
_sym_db.RegisterMessage(LogResult)

Port = _reflection.GeneratedProtocolMessageType('Port', (_message.Message,), dict(
  DESCRIPTOR = _PORT,
  __module__ = 'muscle_manager_protocol_pb2'
  # @@protoc_insertion_point(class_scope:muscle_manager_protocol.Port)
  ))
_sym_db.RegisterMessage(Port)

RegistrationRequest = _reflection.GeneratedProtocolMessageType('RegistrationRequest', (_message.Message,), dict(
  DESCRIPTOR = _REGISTRATIONREQUEST,
  __module__ = 'muscle_manager_protocol_pb2'
  # @@protoc_insertion_point(class_scope:muscle_manager_protocol.RegistrationRequest)
  ))
_sym_db.RegisterMessage(RegistrationRequest)

RegistrationResult = _reflection.GeneratedProtocolMessageType('RegistrationResult', (_message.Message,), dict(
  DESCRIPTOR = _REGISTRATIONRESULT,
  __module__ = 'muscle_manager_protocol_pb2'
  # @@protoc_insertion_point(class_scope:muscle_manager_protocol.RegistrationResult)
  ))
_sym_db.RegisterMessage(RegistrationResult)



_MUSCLEMANAGER = _descriptor.ServiceDescriptor(
  name='MuscleManager',
  full_name='muscle_manager_protocol.MuscleManager',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=978,
  serialized_end=1197,
  methods=[
  _descriptor.MethodDescriptor(
    name='SubmitLogMessage',
    full_name='muscle_manager_protocol.MuscleManager.SubmitLogMessage',
    index=0,
    containing_service=None,
    input_type=_LOGMESSAGE,
    output_type=_LOGRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterInstance',
    full_name='muscle_manager_protocol.MuscleManager.RegisterInstance',
    index=1,
    containing_service=None,
    input_type=_REGISTRATIONREQUEST,
    output_type=_REGISTRATIONRESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MUSCLEMANAGER)

DESCRIPTOR.services_by_name['MuscleManager'] = _MUSCLEMANAGER

# @@protoc_insertion_point(module_scope)