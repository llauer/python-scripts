#!/usr/bin/env python

# goal is to discover clients on the network

# create arp request to the broadcast MAC for IP
# send packet and receive response
# parse the response
# print the result


# import scapy.all as scapy
#
# def scan(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     arp_request.show()
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     broadcast.show()
#     arp_request_broadcast = broadcast/arp_request
#     print(arp_request_broadcast.summary())
#     arp_request_broadcast.show()
#
#     # scapy.ls(scapy.ARP())
#
# scan("10.0.2.1/24")

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print("IP\t\t\tMAC Address\n--------------------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)




scan("10.0.2.1/24")