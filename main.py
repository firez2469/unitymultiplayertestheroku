import socket
import struct
import traceback
import logging
import time
import os
import sys
from subprocess import Popen

print('started')
def messagingInterpretation(msg1):
    return msg1


def sending_and_recieving():
    print("starting connection at:",socket.gethostbyname(socket.gethostname()))
    s = socket.socket()
    socket.setdefaulttimeout(None)
    print('socket created ')
    port = 60000
    try:
        ip = socket.gethostbyname(socket.gethostname())
        s.bind((ip,port))
        s.listen(30)
        print('socket listening...')
    except:
        print('program ended')
    while True:
        try:
            c, addr = s.accept()
            bytes_received = c.recv(4000)
            string_received = bytes_received.decode("utf-8")
            print('received',string_received)

            string_to_send = messagingInterpretation(string_received)
            bytes_to_send = str.encode(string_to_send)
            c.sendall(bytes_to_send)
            c.close()
        except Exception as e:
            logging.error(traceback.format_exc())
            print("error")
            c.sendall(bytearray([]))
            c.close()
            break
sending_and_recieving()

    
