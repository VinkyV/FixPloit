# -*- coding: utf-8 -*-
import socket
import sys
import time

def menu():
    cmd = input('>')
    if cmd == '#help':
        print('#port - PortScanner')
        print('#f - F')
        print('#exit - to exit')
        menu()
    elif cmd == '#port':
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = input('IP:')
        port = int(input('PORT:'))

        def portScanner(port):
            if s.connect_ex((host, port)):
                print('port closed!')
            else:
                print('port opened!')

        portScanner(port)
        menu()
    elif cmd == '#f':
        print('███████╗\n██╔════╝\n█████╗\n██╔══╝\n██║\n╚═╝')
        menu()
    elif cmd == '#exit':
        print('Exiting...')
        quit()
    else:
        print('Command not found! Check commands in #help!')
        menu()

print('\n███████╗         ███████╗\n██╔════╝██╗██╗██╗██╔══██║██╗██████╗██╗██████╗\n█████╗  ╚═╝╚███╬╝███████║██║██╔═██║╚═╝╚═██╔═╝\n██╔══╝  ██╗ ███║ ██╔════╝██║██║ ██║██╗  ██║\n██║     ██║██╬██╗██║     ██║██████║██║  ██║\n╚═╝     ╚═╝╚═╝╚═╝╚═╝     ╚═╝╚═════╝╚═╝  ╚═╝')
print('Welcome to Fixploit v1.0')
print('Write a command!')
menu()