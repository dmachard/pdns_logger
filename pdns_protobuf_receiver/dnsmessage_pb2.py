# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dnsmessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dnsmessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x64nsmessage.proto\"\xdc\t\n\x0cPBDNSMessage\x12 \n\x04type\x18\x01 \x02(\x0e\x32\x12.PBDNSMessage.Type\x12\x11\n\tmessageId\x18\x02 \x01(\x0c\x12\x16\n\x0eserverIdentity\x18\x03 \x01(\x0c\x12\x30\n\x0csocketFamily\x18\x04 \x01(\x0e\x32\x1a.PBDNSMessage.SocketFamily\x12\x34\n\x0esocketProtocol\x18\x05 \x01(\x0e\x32\x1c.PBDNSMessage.SocketProtocol\x12\x0c\n\x04\x66rom\x18\x06 \x01(\x0c\x12\n\n\x02to\x18\x07 \x01(\x0c\x12\x0f\n\x07inBytes\x18\x08 \x01(\x04\x12\x0f\n\x07timeSec\x18\t \x01(\r\x12\x10\n\x08timeUsec\x18\n \x01(\r\x12\n\n\x02id\x18\x0b \x01(\r\x12+\n\x08question\x18\x0c \x01(\x0b\x32\x19.PBDNSMessage.DNSQuestion\x12+\n\x08response\x18\r \x01(\x0b\x32\x19.PBDNSMessage.DNSResponse\x12\x1f\n\x17originalRequestorSubnet\x18\x0e \x01(\x0c\x12\x13\n\x0brequestorId\x18\x0f \x01(\t\x12\x18\n\x10initialRequestId\x18\x10 \x01(\x0c\x12\x10\n\x08\x64\x65viceId\x18\x11 \x01(\x0c\x12\x1b\n\x13newlyObservedDomain\x18\x12 \x01(\x08\x12\x12\n\ndeviceName\x18\x13 \x01(\t\x12\x10\n\x08\x66romPort\x18\x14 \x01(\r\x12\x0e\n\x06toPort\x18\x15 \x01(\r\x1a;\n\x0b\x44NSQuestion\x12\r\n\x05qName\x18\x01 \x01(\t\x12\r\n\x05qType\x18\x02 \x01(\r\x12\x0e\n\x06qClass\x18\x03 \x01(\r\x1a\xe6\x02\n\x0b\x44NSResponse\x12\r\n\x05rcode\x18\x01 \x01(\r\x12,\n\x03rrs\x18\x02 \x03(\x0b\x32\x1f.PBDNSMessage.DNSResponse.DNSRR\x12\x15\n\rappliedPolicy\x18\x03 \x01(\t\x12\x0c\n\x04tags\x18\x04 \x03(\t\x12\x14\n\x0cqueryTimeSec\x18\x05 \x01(\r\x12\x15\n\rqueryTimeUsec\x18\x06 \x01(\r\x12\x33\n\x11\x61ppliedPolicyType\x18\x07 \x01(\x0e\x32\x18.PBDNSMessage.PolicyType\x12\x1c\n\x14\x61ppliedPolicyTrigger\x18\x08 \x01(\t\x12\x18\n\x10\x61ppliedPolicyHit\x18\t \x01(\t\x1a[\n\x05\x44NSRR\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\r\x12\r\n\x05\x63lass\x18\x03 \x01(\r\x12\x0b\n\x03ttl\x18\x04 \x01(\r\x12\r\n\x05rdata\x18\x05 \x01(\x0c\x12\x0b\n\x03udr\x18\x06 \x01(\x08\"d\n\x04Type\x12\x10\n\x0c\x44NSQueryType\x10\x01\x12\x13\n\x0f\x44NSResponseType\x10\x02\x12\x18\n\x14\x44NSOutgoingQueryType\x10\x03\x12\x1b\n\x17\x44NSIncomingResponseType\x10\x04\"#\n\x0cSocketFamily\x12\x08\n\x04INET\x10\x01\x12\t\n\x05INET6\x10\x02\"\"\n\x0eSocketProtocol\x12\x07\n\x03UDP\x10\x01\x12\x07\n\x03TCP\x10\x02\"Y\n\nPolicyType\x12\x0b\n\x07UNKNOWN\x10\x01\x12\t\n\x05QNAME\x10\x02\x12\x0c\n\x08\x43LIENTIP\x10\x03\x12\x0e\n\nRESPONSEIP\x10\x04\x12\x0b\n\x07NSDNAME\x10\x05\x12\x08\n\x04NSIP\x10\x06'
)



_PBDNSMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='PBDNSMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DNSQueryType', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DNSResponseType', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DNSOutgoingQueryType', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DNSIncomingResponseType', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1001,
  serialized_end=1101,
)
_sym_db.RegisterEnumDescriptor(_PBDNSMESSAGE_TYPE)

_PBDNSMESSAGE_SOCKETFAMILY = _descriptor.EnumDescriptor(
  name='SocketFamily',
  full_name='PBDNSMessage.SocketFamily',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INET', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INET6', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1103,
  serialized_end=1138,
)
_sym_db.RegisterEnumDescriptor(_PBDNSMESSAGE_SOCKETFAMILY)

_PBDNSMESSAGE_SOCKETPROTOCOL = _descriptor.EnumDescriptor(
  name='SocketProtocol',
  full_name='PBDNSMessage.SocketProtocol',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UDP', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TCP', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1140,
  serialized_end=1174,
)
_sym_db.RegisterEnumDescriptor(_PBDNSMESSAGE_SOCKETPROTOCOL)

_PBDNSMESSAGE_POLICYTYPE = _descriptor.EnumDescriptor(
  name='PolicyType',
  full_name='PBDNSMessage.PolicyType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QNAME', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLIENTIP', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESPONSEIP', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NSDNAME', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NSIP', index=5, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1176,
  serialized_end=1265,
)
_sym_db.RegisterEnumDescriptor(_PBDNSMESSAGE_POLICYTYPE)


_PBDNSMESSAGE_DNSQUESTION = _descriptor.Descriptor(
  name='DNSQuestion',
  full_name='PBDNSMessage.DNSQuestion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='qName', full_name='PBDNSMessage.DNSQuestion.qName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='qType', full_name='PBDNSMessage.DNSQuestion.qType', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='qClass', full_name='PBDNSMessage.DNSQuestion.qClass', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=579,
  serialized_end=638,
)

_PBDNSMESSAGE_DNSRESPONSE_DNSRR = _descriptor.Descriptor(
  name='DNSRR',
  full_name='PBDNSMessage.DNSResponse.DNSRR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='PBDNSMessage.DNSResponse.DNSRR.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='PBDNSMessage.DNSResponse.DNSRR.type', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='class', full_name='PBDNSMessage.DNSResponse.DNSRR.class', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='PBDNSMessage.DNSResponse.DNSRR.ttl', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rdata', full_name='PBDNSMessage.DNSResponse.DNSRR.rdata', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='udr', full_name='PBDNSMessage.DNSResponse.DNSRR.udr', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=908,
  serialized_end=999,
)

_PBDNSMESSAGE_DNSRESPONSE = _descriptor.Descriptor(
  name='DNSResponse',
  full_name='PBDNSMessage.DNSResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rcode', full_name='PBDNSMessage.DNSResponse.rcode', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rrs', full_name='PBDNSMessage.DNSResponse.rrs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='appliedPolicy', full_name='PBDNSMessage.DNSResponse.appliedPolicy', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='PBDNSMessage.DNSResponse.tags', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='queryTimeSec', full_name='PBDNSMessage.DNSResponse.queryTimeSec', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='queryTimeUsec', full_name='PBDNSMessage.DNSResponse.queryTimeUsec', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='appliedPolicyType', full_name='PBDNSMessage.DNSResponse.appliedPolicyType', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='appliedPolicyTrigger', full_name='PBDNSMessage.DNSResponse.appliedPolicyTrigger', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='appliedPolicyHit', full_name='PBDNSMessage.DNSResponse.appliedPolicyHit', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PBDNSMESSAGE_DNSRESPONSE_DNSRR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=641,
  serialized_end=999,
)

_PBDNSMESSAGE = _descriptor.Descriptor(
  name='PBDNSMessage',
  full_name='PBDNSMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='PBDNSMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='messageId', full_name='PBDNSMessage.messageId', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serverIdentity', full_name='PBDNSMessage.serverIdentity', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='socketFamily', full_name='PBDNSMessage.socketFamily', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='socketProtocol', full_name='PBDNSMessage.socketProtocol', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='from', full_name='PBDNSMessage.from', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to', full_name='PBDNSMessage.to', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inBytes', full_name='PBDNSMessage.inBytes', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeSec', full_name='PBDNSMessage.timeSec', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeUsec', full_name='PBDNSMessage.timeUsec', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='PBDNSMessage.id', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='question', full_name='PBDNSMessage.question', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='PBDNSMessage.response', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='originalRequestorSubnet', full_name='PBDNSMessage.originalRequestorSubnet', index=13,
      number=14, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requestorId', full_name='PBDNSMessage.requestorId', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='initialRequestId', full_name='PBDNSMessage.initialRequestId', index=15,
      number=16, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='PBDNSMessage.deviceId', index=16,
      number=17, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='newlyObservedDomain', full_name='PBDNSMessage.newlyObservedDomain', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deviceName', full_name='PBDNSMessage.deviceName', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fromPort', full_name='PBDNSMessage.fromPort', index=19,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='toPort', full_name='PBDNSMessage.toPort', index=20,
      number=21, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PBDNSMESSAGE_DNSQUESTION, _PBDNSMESSAGE_DNSRESPONSE, ],
  enum_types=[
    _PBDNSMESSAGE_TYPE,
    _PBDNSMESSAGE_SOCKETFAMILY,
    _PBDNSMESSAGE_SOCKETPROTOCOL,
    _PBDNSMESSAGE_POLICYTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=1265,
)

_PBDNSMESSAGE_DNSQUESTION.containing_type = _PBDNSMESSAGE
_PBDNSMESSAGE_DNSRESPONSE_DNSRR.containing_type = _PBDNSMESSAGE_DNSRESPONSE
_PBDNSMESSAGE_DNSRESPONSE.fields_by_name['rrs'].message_type = _PBDNSMESSAGE_DNSRESPONSE_DNSRR
_PBDNSMESSAGE_DNSRESPONSE.fields_by_name['appliedPolicyType'].enum_type = _PBDNSMESSAGE_POLICYTYPE
_PBDNSMESSAGE_DNSRESPONSE.containing_type = _PBDNSMESSAGE
_PBDNSMESSAGE.fields_by_name['type'].enum_type = _PBDNSMESSAGE_TYPE
_PBDNSMESSAGE.fields_by_name['socketFamily'].enum_type = _PBDNSMESSAGE_SOCKETFAMILY
_PBDNSMESSAGE.fields_by_name['socketProtocol'].enum_type = _PBDNSMESSAGE_SOCKETPROTOCOL
_PBDNSMESSAGE.fields_by_name['question'].message_type = _PBDNSMESSAGE_DNSQUESTION
_PBDNSMESSAGE.fields_by_name['response'].message_type = _PBDNSMESSAGE_DNSRESPONSE
_PBDNSMESSAGE_TYPE.containing_type = _PBDNSMESSAGE
_PBDNSMESSAGE_SOCKETFAMILY.containing_type = _PBDNSMESSAGE
_PBDNSMESSAGE_SOCKETPROTOCOL.containing_type = _PBDNSMESSAGE
_PBDNSMESSAGE_POLICYTYPE.containing_type = _PBDNSMESSAGE
DESCRIPTOR.message_types_by_name['PBDNSMessage'] = _PBDNSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PBDNSMessage = _reflection.GeneratedProtocolMessageType('PBDNSMessage', (_message.Message,), {

  'DNSQuestion' : _reflection.GeneratedProtocolMessageType('DNSQuestion', (_message.Message,), {
    'DESCRIPTOR' : _PBDNSMESSAGE_DNSQUESTION,
    '__module__' : 'dnsmessage_pb2'
    # @@protoc_insertion_point(class_scope:PBDNSMessage.DNSQuestion)
    })
  ,

  'DNSResponse' : _reflection.GeneratedProtocolMessageType('DNSResponse', (_message.Message,), {

    'DNSRR' : _reflection.GeneratedProtocolMessageType('DNSRR', (_message.Message,), {
      'DESCRIPTOR' : _PBDNSMESSAGE_DNSRESPONSE_DNSRR,
      '__module__' : 'dnsmessage_pb2'
      # @@protoc_insertion_point(class_scope:PBDNSMessage.DNSResponse.DNSRR)
      })
    ,
    'DESCRIPTOR' : _PBDNSMESSAGE_DNSRESPONSE,
    '__module__' : 'dnsmessage_pb2'
    # @@protoc_insertion_point(class_scope:PBDNSMessage.DNSResponse)
    })
  ,
  'DESCRIPTOR' : _PBDNSMESSAGE,
  '__module__' : 'dnsmessage_pb2'
  # @@protoc_insertion_point(class_scope:PBDNSMessage)
  })
_sym_db.RegisterMessage(PBDNSMessage)
_sym_db.RegisterMessage(PBDNSMessage.DNSQuestion)
_sym_db.RegisterMessage(PBDNSMessage.DNSResponse)
_sym_db.RegisterMessage(PBDNSMessage.DNSResponse.DNSRR)


# @@protoc_insertion_point(module_scope)
