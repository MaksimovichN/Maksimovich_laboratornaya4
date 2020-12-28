from dataclasses import dataclass
import socket, struct, threading, time
import json
from msg import *
from controller import *

HOST = 'localhost'
PORT = 12345

def ProcessReceive():
    while True:
        try:
            msg = GetMsg(Message.ClientID)['messages']
            if len(msg>0):
                print('Your messages: ' + GetMsg(Message.ClientID)['messages'])
        except Exception as e:
            pass
        time.sleep(10)

def Client():
    Message.SendMessage(M_BROKER, M_INIT)

    t = threading.Thread(target=ProcessReceive)
    t.start()
    while True: 
        n = int(input("1. Отправить сообщение \n2. Получить сообщения\n"))
        if (n == 1):
            s = input("Введите сообщение\n")
            id = M_ALL
            n1 = int(input("1. Отправить сообщение клиенту \n2. Отправить сообщение всем\n"))
            if (n1 == 1): 
                id = int(input("Введите id \n"))
            SendMsg(Message.ClientID, s, id)
        elif (n == 2):
            print(GetMsg(Message.ClientID)['messages'])
Client()