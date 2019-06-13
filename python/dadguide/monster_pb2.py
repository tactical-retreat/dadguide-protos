# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/monster.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/monster.proto',
  package='dadguide',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14protos/monster.proto\x12\x08\x64\x61\x64guide\"@\n\x0e\x43rossServerInt\x12\x0e\n\x02jp\x18\x01 \x01(\x05R\x02jp\x12\x0e\n\x02na\x18\x02 \x01(\x05R\x02na\x12\x0e\n\x02kr\x18\x03 \x01(\x05R\x02kr\"C\n\x11\x43rossServerString\x12\x0e\n\x02jp\x18\x01 \x01(\tR\x02jp\x12\x0e\n\x02na\x18\x02 \x01(\tR\x02na\x12\x0e\n\x02kr\x18\x03 \x01(\tR\x02kr\"A\n\x05\x43urve\x12\x10\n\x03max\x18\x01 \x01(\x05R\x03max\x12\x10\n\x03min\x18\x02 \x01(\x05R\x03min\x12\x14\n\x05scale\x18\x03 \x01(\x02R\x05scale\"\xd7\x03\n\x07Monster\x12\x1d\n\nmonster_no\x18\x01 \x01(\x05R\tmonsterNo\x12\x37\n\nmonster_id\x18\x02 \x01(\x0b\x32\x18.dadguide.CrossServerIntR\tmonsterId\x12/\n\x04name\x18\x03 \x01(\x0b\x32\x1b.dadguide.CrossServerStringR\x04name\x12\x1f\n\x02hp\x18\x04 \x01(\x0b\x32\x0f.dadguide.CurveR\x02hp\x12!\n\x03\x61tk\x18\x05 \x01(\x0b\x32\x0f.dadguide.CurveR\x03\x61tk\x12!\n\x03rcv\x18\x06 \x01(\x0b\x32\x0f.dadguide.CurveR\x03rcv\x12\x12\n\x04\x63ost\x18\x07 \x01(\x05R\x04\x63ost\x12\x10\n\x03\x65xp\x18\x08 \x01(\x05R\x03\x65xp\x12\x14\n\x05level\x18\t \x01(\x05R\x05level\x12\x16\n\x06rarity\x18\n \x01(\x05R\x06rarity\x12,\n\x06type_1\x18\x0b \x01(\x0e\x32\x15.dadguide.MonsterTypeR\x05type1\x12,\n\x06type_2\x18\x0c \x01(\x0e\x32\x15.dadguide.MonsterTypeR\x05type2\x12,\n\x06type_3\x18\r \x01(\x0e\x32\x15.dadguide.MonsterTypeR\x05type3*:\n\x0bMonsterType\x12\x18\n\x14UNKNOWN_MONSTER_TYPE\x10\x00\x12\x07\n\x03GOD\x10\x01\x12\x08\n\x04WORK\x10\x02*0\n\tAwakening\x12\x15\n\x11UNKNOWN_AWAKENING\x10\x00\x12\x0c\n\x08HP_BOOST\x10\x01\x62\x06proto3')
)

_MONSTERTYPE = _descriptor.EnumDescriptor(
  name='MonsterType',
  full_name='dadguide.MonsterType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_MONSTER_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=710,
  serialized_end=768,
)
_sym_db.RegisterEnumDescriptor(_MONSTERTYPE)

MonsterType = enum_type_wrapper.EnumTypeWrapper(_MONSTERTYPE)
_AWAKENING = _descriptor.EnumDescriptor(
  name='Awakening',
  full_name='dadguide.Awakening',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_AWAKENING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HP_BOOST', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=770,
  serialized_end=818,
)
_sym_db.RegisterEnumDescriptor(_AWAKENING)

Awakening = enum_type_wrapper.EnumTypeWrapper(_AWAKENING)
UNKNOWN_MONSTER_TYPE = 0
GOD = 1
WORK = 2
UNKNOWN_AWAKENING = 0
HP_BOOST = 1



_CROSSSERVERINT = _descriptor.Descriptor(
  name='CrossServerInt',
  full_name='dadguide.CrossServerInt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jp', full_name='dadguide.CrossServerInt.jp', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='jp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='na', full_name='dadguide.CrossServerInt.na', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='na', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kr', full_name='dadguide.CrossServerInt.kr', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='kr', file=DESCRIPTOR),
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
  serialized_start=34,
  serialized_end=98,
)


_CROSSSERVERSTRING = _descriptor.Descriptor(
  name='CrossServerString',
  full_name='dadguide.CrossServerString',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jp', full_name='dadguide.CrossServerString.jp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='jp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='na', full_name='dadguide.CrossServerString.na', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='na', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kr', full_name='dadguide.CrossServerString.kr', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='kr', file=DESCRIPTOR),
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
  serialized_start=100,
  serialized_end=167,
)


_CURVE = _descriptor.Descriptor(
  name='Curve',
  full_name='dadguide.Curve',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max', full_name='dadguide.Curve.max', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='max', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min', full_name='dadguide.Curve.min', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='min', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='dadguide.Curve.scale', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='scale', file=DESCRIPTOR),
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
  serialized_start=169,
  serialized_end=234,
)


_MONSTER = _descriptor.Descriptor(
  name='Monster',
  full_name='dadguide.Monster',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='monster_no', full_name='dadguide.Monster.monster_no', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='monsterNo', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='monster_id', full_name='dadguide.Monster.monster_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='monsterId', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dadguide.Monster.name', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hp', full_name='dadguide.Monster.hp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='atk', full_name='dadguide.Monster.atk', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='atk', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rcv', full_name='dadguide.Monster.rcv', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rcv', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost', full_name='dadguide.Monster.cost', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='cost', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp', full_name='dadguide.Monster.exp', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='exp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='dadguide.Monster.level', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='level', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rarity', full_name='dadguide.Monster.rarity', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rarity', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_1', full_name='dadguide.Monster.type_1', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type1', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_2', full_name='dadguide.Monster.type_2', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type2', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_3', full_name='dadguide.Monster.type_3', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type3', file=DESCRIPTOR),
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
  serialized_start=237,
  serialized_end=708,
)

_MONSTER.fields_by_name['monster_id'].message_type = _CROSSSERVERINT
_MONSTER.fields_by_name['name'].message_type = _CROSSSERVERSTRING
_MONSTER.fields_by_name['hp'].message_type = _CURVE
_MONSTER.fields_by_name['atk'].message_type = _CURVE
_MONSTER.fields_by_name['rcv'].message_type = _CURVE
_MONSTER.fields_by_name['type_1'].enum_type = _MONSTERTYPE
_MONSTER.fields_by_name['type_2'].enum_type = _MONSTERTYPE
_MONSTER.fields_by_name['type_3'].enum_type = _MONSTERTYPE
DESCRIPTOR.message_types_by_name['CrossServerInt'] = _CROSSSERVERINT
DESCRIPTOR.message_types_by_name['CrossServerString'] = _CROSSSERVERSTRING
DESCRIPTOR.message_types_by_name['Curve'] = _CURVE
DESCRIPTOR.message_types_by_name['Monster'] = _MONSTER
DESCRIPTOR.enum_types_by_name['MonsterType'] = _MONSTERTYPE
DESCRIPTOR.enum_types_by_name['Awakening'] = _AWAKENING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CrossServerInt = _reflection.GeneratedProtocolMessageType('CrossServerInt', (_message.Message,), dict(
  DESCRIPTOR = _CROSSSERVERINT,
  __module__ = 'protos.monster_pb2'
  # @@protoc_insertion_point(class_scope:dadguide.CrossServerInt)
  ))
_sym_db.RegisterMessage(CrossServerInt)

CrossServerString = _reflection.GeneratedProtocolMessageType('CrossServerString', (_message.Message,), dict(
  DESCRIPTOR = _CROSSSERVERSTRING,
  __module__ = 'protos.monster_pb2'
  # @@protoc_insertion_point(class_scope:dadguide.CrossServerString)
  ))
_sym_db.RegisterMessage(CrossServerString)

Curve = _reflection.GeneratedProtocolMessageType('Curve', (_message.Message,), dict(
  DESCRIPTOR = _CURVE,
  __module__ = 'protos.monster_pb2'
  # @@protoc_insertion_point(class_scope:dadguide.Curve)
  ))
_sym_db.RegisterMessage(Curve)

Monster = _reflection.GeneratedProtocolMessageType('Monster', (_message.Message,), dict(
  DESCRIPTOR = _MONSTER,
  __module__ = 'protos.monster_pb2'
  # @@protoc_insertion_point(class_scope:dadguide.Monster)
  ))
_sym_db.RegisterMessage(Monster)


# @@protoc_insertion_point(module_scope)
