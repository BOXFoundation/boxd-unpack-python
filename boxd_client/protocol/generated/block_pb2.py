# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: block.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='block.proto',
  package='corepb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x62lock.proto\x12\x06\x63orepb\"\x9f\x02\n\x0b\x42lockHeader\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x17\n\x0fprev_block_hash\x18\x02 \x01(\x0c\x12\x10\n\x08txs_root\x18\x03 \x01(\x0c\x12\x19\n\x11internal_txs_root\x18\x04 \x01(\x0c\x12\x11\n\tutxo_root\x18\x05 \x01(\x0c\x12\x14\n\x0creceipt_hash\x18\x06 \x01(\x0c\x12\x12\n\ntime_stamp\x18\x07 \x01(\x03\x12\r\n\x05magic\x18\x08 \x01(\r\x12\x14\n\x0c\x64ynasty_hash\x18\t \x01(\x0c\x12\x11\n\troot_hash\x18\n \x01(\x0c\x12\x0e\n\x06height\x18\x0b \x01(\r\x12\x10\n\x08gas_used\x18\x0c \x01(\x04\x12\x13\n\x0b\x62ook_keeper\x18\r \x01(\x0c\x12\r\n\x05\x62loom\x18\x0e \x01(\x0c\"4\n\x10IrreversibleInfo\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\x12\n\nsignatures\x18\x02 \x03(\x0c\"\xc1\x01\n\x05\x42lock\x12#\n\x06header\x18\x01 \x01(\x0b\x32\x13.corepb.BlockHeader\x12 \n\x03txs\x18\x02 \x03(\x0b\x32\x13.corepb.Transaction\x12)\n\x0cinternal_txs\x18\x03 \x03(\x0b\x32\x13.corepb.Transaction\x12\x11\n\tsignature\x18\x04 \x01(\x0c\x12\x33\n\x11irreversible_info\x18\x05 \x01(\x0b\x32\x18.corepb.IrreversibleInfo\"\x94\x01\n\x0bTransaction\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x19\n\x03vin\x18\x02 \x03(\x0b\x32\x0c.corepb.TxIn\x12\x1b\n\x04vout\x18\x03 \x03(\x0b\x32\r.corepb.TxOut\x12\x1a\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x0c.corepb.Data\x12\r\n\x05magic\x18\x05 \x01(\r\x12\x11\n\tlock_time\x18\x06 \x01(\x03\"V\n\x04TxIn\x12(\n\x0eprev_out_point\x18\x01 \x01(\x0b\x32\x10.corepb.OutPoint\x12\x12\n\nscript_sig\x18\x02 \x01(\x0c\x12\x10\n\x08sequence\x18\x03 \x01(\r\".\n\x05TxOut\x12\r\n\x05value\x18\x01 \x01(\x04\x12\x16\n\x0escript_pub_key\x18\x02 \x01(\x0c\"\'\n\x08OutPoint\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\r\n\x05index\x18\x02 \x01(\r\"%\n\x04\x44\x61ta\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x62\x06proto3')
)




_BLOCKHEADER = _descriptor.Descriptor(
  name='BlockHeader',
  full_name='corepb.BlockHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='corepb.BlockHeader.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prev_block_hash', full_name='corepb.BlockHeader.prev_block_hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txs_root', full_name='corepb.BlockHeader.txs_root', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal_txs_root', full_name='corepb.BlockHeader.internal_txs_root', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='utxo_root', full_name='corepb.BlockHeader.utxo_root', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receipt_hash', full_name='corepb.BlockHeader.receipt_hash', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='corepb.BlockHeader.time_stamp', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='magic', full_name='corepb.BlockHeader.magic', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dynasty_hash', full_name='corepb.BlockHeader.dynasty_hash', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='root_hash', full_name='corepb.BlockHeader.root_hash', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='corepb.BlockHeader.height', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas_used', full_name='corepb.BlockHeader.gas_used', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='book_keeper', full_name='corepb.BlockHeader.book_keeper', index=12,
      number=13, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bloom', full_name='corepb.BlockHeader.bloom', index=13,
      number=14, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=24,
  serialized_end=311,
)


_IRREVERSIBLEINFO = _descriptor.Descriptor(
  name='IrreversibleInfo',
  full_name='corepb.IrreversibleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='corepb.IrreversibleInfo.hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signatures', full_name='corepb.IrreversibleInfo.signatures', index=1,
      number=2, type=12, cpp_type=9, label=3,
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
  serialized_start=313,
  serialized_end=365,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='corepb.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='corepb.Block.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txs', full_name='corepb.Block.txs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal_txs', full_name='corepb.Block.internal_txs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='corepb.Block.signature', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='irreversible_info', full_name='corepb.Block.irreversible_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=368,
  serialized_end=561,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='corepb.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='corepb.Transaction.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vin', full_name='corepb.Transaction.vin', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vout', full_name='corepb.Transaction.vout', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='corepb.Transaction.data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='magic', full_name='corepb.Transaction.magic', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lock_time', full_name='corepb.Transaction.lock_time', index=5,
      number=6, type=3, cpp_type=2, label=1,
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
  serialized_start=564,
  serialized_end=712,
)


_TXIN = _descriptor.Descriptor(
  name='TxIn',
  full_name='corepb.TxIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prev_out_point', full_name='corepb.TxIn.prev_out_point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script_sig', full_name='corepb.TxIn.script_sig', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='corepb.TxIn.sequence', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=714,
  serialized_end=800,
)


_TXOUT = _descriptor.Descriptor(
  name='TxOut',
  full_name='corepb.TxOut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='corepb.TxOut.value', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script_pub_key', full_name='corepb.TxOut.script_pub_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=802,
  serialized_end=848,
)


_OUTPOINT = _descriptor.Descriptor(
  name='OutPoint',
  full_name='corepb.OutPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='corepb.OutPoint.hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='corepb.OutPoint.index', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=850,
  serialized_end=889,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='corepb.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='corepb.Data.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='corepb.Data.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=891,
  serialized_end=928,
)

_BLOCK.fields_by_name['header'].message_type = _BLOCKHEADER
_BLOCK.fields_by_name['txs'].message_type = _TRANSACTION
_BLOCK.fields_by_name['internal_txs'].message_type = _TRANSACTION
_BLOCK.fields_by_name['irreversible_info'].message_type = _IRREVERSIBLEINFO
_TRANSACTION.fields_by_name['vin'].message_type = _TXIN
_TRANSACTION.fields_by_name['vout'].message_type = _TXOUT
_TRANSACTION.fields_by_name['data'].message_type = _DATA
_TXIN.fields_by_name['prev_out_point'].message_type = _OUTPOINT
DESCRIPTOR.message_types_by_name['BlockHeader'] = _BLOCKHEADER
DESCRIPTOR.message_types_by_name['IrreversibleInfo'] = _IRREVERSIBLEINFO
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['TxIn'] = _TXIN
DESCRIPTOR.message_types_by_name['TxOut'] = _TXOUT
DESCRIPTOR.message_types_by_name['OutPoint'] = _OUTPOINT
DESCRIPTOR.message_types_by_name['Data'] = _DATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlockHeader = _reflection.GeneratedProtocolMessageType('BlockHeader', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKHEADER,
  __module__ = 'block_pb2'
  # @@protoc_insertion_point(class_scope:corepb.BlockHeader)
  ))
_sym_db.RegisterMessage(BlockHeader)

IrreversibleInfo = _reflection.GeneratedProtocolMessageType('IrreversibleInfo', (_message.Message,), dict(
  DESCRIPTOR = _IRREVERSIBLEINFO,
  __module__ = 'block_pb2'
  # @@protoc_insertion_point(class_scope:corepb.IrreversibleInfo)
  ))
_sym_db.RegisterMessage(IrreversibleInfo)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'block_pb2'
  # @@protoc_insertion_point(class_scope:corepb.Block)
  ))
_sym_db.RegisterMessage(Block)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'block_pb2'
  # @@protoc_insertion_point(class_scope:corepb.Transaction)
  ))
_sym_db.RegisterMessage(Transaction)

TxIn = _reflection.GeneratedProtocolMessageType('TxIn', (_message.Message,), dict(
  DESCRIPTOR = _TXIN,
  __module__ = 'block_pb2'
  # @@protoc_insertion_point(class_scope:corepb.TxIn)
  ))
_sym_db.RegisterMessage(TxIn)

TxOut = _reflection.GeneratedProtocolMessageType('TxOut', (_message.Message,), dict(
  DESCRIPTOR = _TXOUT,
  __module__ = 'block_pb2'
  # @@protoc_insertion_point(class_scope:corepb.TxOut)
  ))
_sym_db.RegisterMessage(TxOut)

OutPoint = _reflection.GeneratedProtocolMessageType('OutPoint', (_message.Message,), dict(
  DESCRIPTOR = _OUTPOINT,
  __module__ = 'block_pb2'
  # @@protoc_insertion_point(class_scope:corepb.OutPoint)
  ))
_sym_db.RegisterMessage(OutPoint)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
  DESCRIPTOR = _DATA,
  __module__ = 'block_pb2'
  # @@protoc_insertion_point(class_scope:corepb.Data)
  ))
_sym_db.RegisterMessage(Data)


# @@protoc_insertion_point(module_scope)
