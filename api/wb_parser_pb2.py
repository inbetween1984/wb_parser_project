# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: wb_parser.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'wb_parser.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fwb_parser.proto\x12\x08wbparser\"\x1e\n\x0c\x42\x61tchRequest\x12\x0e\n\x06nm_ids\x18\x01 \x03(\x05\"L\n\x0fProductResponse\x12\r\n\x05nm_id\x18\x01 \x01(\x05\x12\r\n\x05price\x18\x02 \x01(\x02\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\";\n\rBatchResponse\x12*\n\x07results\x18\x01 \x03(\x0b\x32\x19.wbparser.ProductResponse2G\n\x08WBParser\x12;\n\x08GetPrice\x12\x16.wbparser.BatchRequest\x1a\x17.wbparser.BatchResponseB\x0cZ\n./wbparserb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wb_parser_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\n./wbparser'
  _globals['_BATCHREQUEST']._serialized_start=29
  _globals['_BATCHREQUEST']._serialized_end=59
  _globals['_PRODUCTRESPONSE']._serialized_start=61
  _globals['_PRODUCTRESPONSE']._serialized_end=137
  _globals['_BATCHRESPONSE']._serialized_start=139
  _globals['_BATCHRESPONSE']._serialized_end=198
  _globals['_WBPARSER']._serialized_start=200
  _globals['_WBPARSER']._serialized_end=271
# @@protoc_insertion_point(module_scope)
