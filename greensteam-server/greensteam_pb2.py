# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greensteam.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10greensteam.proto\"^\n\x04Game\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10\x64ownloadQuantity\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x19\n\x11reviewsPercentage\x18\x05 \x01(\x05\"B\n\tPublisher\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x05games\x18\x02 \x03(\x0b\x32\x05.Game\x12\x11\n\tfollowers\x18\x03 \x01(\x05\"O\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x07library\x18\x02 \x03(\x0b\x32\x05.Game\x12\x0b\n\x03\x62io\x18\x03 \x01(\t\x12\x14\n\x0c\x61\x63hievements\x18\x04 \x01(\x05\"E\n\x07\x43omment\x12\x12\n\nauthorName\x18\x01 \x01(\t\x12\x15\n\rrecomendation\x18\x02 \x01(\x08\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"^\n\x07Message\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x14\n\x0cobfReference\x18\x03 \x01(\t\x12\x10\n\x08methodId\x18\x04 \x01(\t\x12\x11\n\targuments\x18\x05 \x01(\x0c\x42\x16\n\x14\x63om.greensteam.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greensteam_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.greensteam.proto'
  _globals['_GAME']._serialized_start=20
  _globals['_GAME']._serialized_end=114
  _globals['_PUBLISHER']._serialized_start=116
  _globals['_PUBLISHER']._serialized_end=182
  _globals['_USER']._serialized_start=184
  _globals['_USER']._serialized_end=263
  _globals['_COMMENT']._serialized_start=265
  _globals['_COMMENT']._serialized_end=334
  _globals['_MESSAGE']._serialized_start=336
  _globals['_MESSAGE']._serialized_end=430
# @@protoc_insertion_point(module_scope)
