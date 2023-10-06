from remove_non_ascii import remove_non_ascii
from uasyncio import StreamReader, wait_for_ms, TimeoutError
from machine import Pin, UART
from config import rs_rx_pin, rs_tx_pin, verbose

timeout = 1000
uart = UART(0, baudrate=9600, tx=Pin(rs_tx_pin), rx=Pin(rs_rx_pin))
sreader = StreamReader(uart)

async def rs_send(message):
    if verbose:
        print('rs write: ', message)
    uart.write('\r*' + message + '#\r')
    try:
        await wait_for_ms(sreader.readline(), 500)
        rcv_char = await wait_for_ms(sreader.readline(), 500)
        if rcv_char:
            resp = remove_non_ascii(rcv_char).decode("ascii")
            resp = resp.strip().lower()
            if resp.startswith('*'):
                resp = resp[:-1][1:]
            if verbose:
                print('rs read: ', resp)
            return resp
        if verbose:
            print('rs read: EMPTY')
        return ''
    except TimeoutError:
        if verbose:
            print('rs read: TIMEOUT')
        return ''
