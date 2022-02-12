
import nmap
import uuid
from tkinter import font
import pyfiglet
import colorama
from colorama import Fore ,Back ,Style
import webbrowser
from tqdm import tqdm, trange
from time import sleep
import sys
import subprocess
import argparse
import random
import time
import re
import scapy.all as scapy
import argparse
sleep(1)
txt = pyfiglet.figlet_format("@ al _ sh _ 136",font="big")
print(Fore.RED +txt)
sleep(0.5)
print("")
print("")
print(   Fore.CYAN    +'                      Welcome....thx to use my tool ')
print("")
print("")
sleep(0.5)
print("                       created by   иasser Alshaqsi")

sleep(0.8)
bar = trange(100)
for i in bar:
    sleep(0.01)
sleep(1) 
print("")  
print("")  
print(   Fore.BLUE      +'                   follow me on instagram for more tool! ')
webbrowser.open("https://www.instagram.com/al_sh_136")
sleep(1)
bar = trange(100)
for i in bar:
    sleep(0.03)

print(Fore.WHITE +"") 
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Sepcify target ip or ip range")
    options = parser.parse_args()
    return  options

def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_packet = broadcast_packet/arp_packet
    answered_list = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]
    client_list = []

    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)

    return client_list

def print_result(scan_list):
    print("IP\t\t\tMAC\n----------------------------------------")
    for client in scan_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
result_list = scan(options.target)
print_result(result_list)