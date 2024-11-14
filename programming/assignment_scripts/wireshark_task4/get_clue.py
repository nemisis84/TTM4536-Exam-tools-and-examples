from scapy.all import *

pkts = rdpcap('communication.pcap')
for pkt in pkts:
    if Raw in pkt:
        payload = pkt[Raw].load.decode(errors='ignore')
        if 'password' in payload.lower():
            print(f"{pkt[IP].src} -> {pkt[IP].dst}")
            print(payload)