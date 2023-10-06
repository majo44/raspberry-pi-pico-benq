def remove_non_ascii(s):
    def remove_non_ascii_byte_array(s):
        ba = bytearray()
        for b in s:
            if b < 0x7F:
                ba.append(b)
        return ba

    def remove_non_ascii_bytes(s):
        o = b""
        for b in s:
            if b < 0x7F:
                o += bytes(chr(b), "ascii")
        return o

    def remove_non_ascii_char(s):
        o = ""
        for c in s:
            if ord(c) < 0x7F:
                o += c
        return o

    if isinstance(s, bytearray): return remove_non_ascii_byte_array(s)
    if isinstance(s, bytes):
        return remove_non_ascii_bytes(s)
    else:
        return remove_non_ascii_char(s)
