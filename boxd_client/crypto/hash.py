#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashlib import sha256
from binascii import hexlify, unhexlify
from utilitybelt import is_hex

def bin_sha256(bin_s):
    return sha256(bin_s).digest()

def bin_checksum(bin_s):
    """ Takes in a binary string and returns a checksum. """
    return bin_sha256(bin_sha256(bin_s))[:4]

def bin_double_sha256(bin_s):
    return bin_sha256(bin_sha256(bin_s))

def bin_hash160(s, hex_format=False):
    """ s is in hex or binary format
    """
    if hex_format and is_hex(s):
        s = unhexlify(s)
    return hashlib.new('ripemd160', bin_sha256(s)).digest()

def hex_hash160(s, hex_format=False):
    """ s is in hex or binary format
    """
    if hex_format and is_hex(s):
        s = unhexlify(s)
    return hexlify(bin_hash160(s))

def reverse_hash(hash, hex_format=True):
    """ hash is in hex or binary format
    """
    if not hex_format:
        hash = hexlify(hash)
    return "".join(reversed([hash[i:i+2] for i in range(0, len(hash), 2)]))