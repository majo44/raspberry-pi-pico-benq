from typing import Any

def country(*args, **kwargs) -> Any: ...
def bootsel_button(*args, **kwargs) -> Any: ...

class Flash:
    def readblocks(self, *args, **kwargs) -> Any: ...
    def writeblocks(self, *args, **kwargs) -> Any: ...
    def ioctl(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class PIO:
    JOIN_TX: int
    JOIN_NONE: int
    JOIN_RX: int
    SHIFT_LEFT: int
    OUT_HIGH: int
    OUT_LOW: int
    SHIFT_RIGHT: int
    IN_LOW: int
    IRQ_SM3: int
    IN_HIGH: int
    IRQ_SM2: int
    IRQ_SM0: int
    IRQ_SM1: int
    def state_machine(self, *args, **kwargs) -> Any: ...
    def remove_program(self, *args, **kwargs) -> Any: ...
    def irq(self, *args, **kwargs) -> Any: ...
    def add_program(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class StateMachine:
    def irq(self, *args, **kwargs) -> Any: ...
    def put(self, *args, **kwargs) -> Any: ...
    def restart(self, *args, **kwargs) -> Any: ...
    def rx_fifo(self, *args, **kwargs) -> Any: ...
    def tx_fifo(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def exec(self, *args, **kwargs) -> Any: ...
    def get(self, *args, **kwargs) -> Any: ...
    def active(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...
