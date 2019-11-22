""" dummy serial module to print all data meant to output on a serial UART connection """
import struct

class Serial:
    def __init__(self, port=None, baudrate=None, timeout=None, interCharTimeout=None):
        print('port requested:', port)
        print('baudrate requested:', baudrate)
        print('timeout requested:', timeout)
        print('interCharTimeout requested:', interCharTimeout)

    def write(self, data):
        print('received:', data)

    def read(self, num_bytes):
        if num_bytes == 1:
            # print('sent:', bytes([0xff]))
            return bytes([0xff])
        return bytearray(num_bytes)

    def readline(self):
        return b'dummy line'

    def is_open(self):
        return True

    def close(self):
        pass

    def flushInput(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *exec):
        return False
