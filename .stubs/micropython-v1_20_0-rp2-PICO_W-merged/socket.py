"""
Module: 'socket' on micropython-v1.20-rp2-PICO_W
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20', 'build': '', 'ver': 'v1.20', 'port': 'rp2', 'board': 'PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.12.2
from typing import Any

SOCK_RAW = 3  # type: int
SOCK_DGRAM = 2  # type: int
SO_REUSEADDR = 4  # type: int
SOCK_STREAM = 1  # type: int
SOL_SOCKET = 1  # type: int
AF_INET6 = 10  # type: int
AF_INET = 2  # type: int
IP_DROP_MEMBERSHIP = 1025  # type: int
IPPROTO_IP = 0  # type: int
IP_ADD_MEMBERSHIP = 1024  # type: int


def reset(*args, **kwargs) -> Any:
    ...


def print_pcbs(*args, **kwargs) -> Any:
    ...


def getaddrinfo(*args, **kwargs) -> Any:
    ...


def callback(*args, **kwargs) -> Any:
    ...


class socket:
    def recvfrom(self, *args, **kwargs) -> Any:
        ...

    def recv(self, *args, **kwargs) -> Any:
        ...

    def makefile(self, *args, **kwargs) -> Any:
        ...

    def listen(self, *args, **kwargs) -> Any:
        ...

    def settimeout(self, *args, **kwargs) -> Any:
        ...

    def sendall(self, *args, **kwargs) -> Any:
        ...

    def setsockopt(self, *args, **kwargs) -> Any:
        ...

    def setblocking(self, *args, **kwargs) -> Any:
        ...

    def sendto(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    def connect(self, *args, **kwargs) -> Any:
        ...

    def send(self, *args, **kwargs) -> Any:
        ...

    def bind(self, *args, **kwargs) -> Any:
        ...

    def accept(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
