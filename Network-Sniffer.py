import scapy.all as scapy
import time

def sniff_packets(interface, filter_protocol=None, filter_port=None, duration=None, source_ip=None, destination_ip=None):
    print(f"Sniffing packets on interface {interface}...")
    if duration:
        timeout = time.time() + duration
    else:
        timeout = None

    while True:
        if timeout and time.time() > timeout:
            break

        packet = scapy.sniff(iface=interface, count=1)[0]
        process_packet(packet, filter_protocol, filter_port, source_ip, destination_ip)

def process_packet(packet, filter_protocol=None, filter_port=None, source_ip=None, destination_ip=None):
    if packet.haslayer(scapy.IP):
        source_ip = packet[scapy.IP].src
        destination_ip = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto

        if (filter_protocol is None or protocol == filter_protocol) and (filter_port is None or source_port == filter_port) and (source_ip is None or source_ip == source_ip) and (destination_ip is None or destination_ip == destination_ip):
            print(f"IP Packet - Source: {source_ip}, Destination: {destination_ip}, Protocol: {protocol}")

    if packet.haslayer(scapy.TCP):
        source_port = packet[scapy.TCP].sport
        destination_port = packet[scapy.TCP].dport
        flags = packet.sprintf("%TCP.flags%")

        if (filter_port is None or source_port == filter_port):
            print(f"TCP Packet - Source Port: {source_port}, Destination Port: {destination_port}, Flags: {flags}")

    if packet.haslayer(scapy.UDP):
        source_port = packet[scapy.UDP].sport
        destination_port = packet[scapy.UDP].dport

        if (filter_port is None or source_port == filter_port):
            print(f"UDP Packet - Source Port: {source_port}, Destination Port: {destination_port}")

    if packet.haslayer(scapy.Raw):
        payload = packet[scapy.Raw].load
        print(f"Packet Payload: {payload}")

    # Log the packet to a file
    with open("packet_log.txt", "a") as log_file:
        log_file.write(str(packet) + "\n")

def start_sniffer():
    print("🍉 ⋆ 🍎  🎀  Ｗｅｌｃｏｍｅ░ｔｏ░ｔｈｅ░Ｂａｓｉｃ░Ｎｅｔｗｏｒｋ░Ｓｎｉｆｆｅｒ░（RAHUL-Ｎｊ）　（佳鉛ゾ唄け　う　り　）  🎀  🍎 ⋆ 🍉")
    interface = input(" 🍬👮  𝐄𝐍𝐓𝐄𝐑  🐺👮 the network interface (e.g., eth0, wlan0): ")
    filter_protocol = input(" 🍬👮  𝐄𝐍𝐓𝐄𝐑  🐺👮  the protocol to filter (e.g., TCP, UDP, or press Enter for all): ")
    filter_port = input(" 🍬👮  𝐄𝐍𝐓𝐄𝐑  🐺👮  the port to filter (e.g., 80, or press Enter for all): ")
    source_ip = input(" 🍬👮  𝐄𝐍𝐓𝐄𝐑  🐺👮  the source IP address to filter (or press Enter for all): ")
    destination_ip = input(" 🍬👮  𝐄𝐍𝐓𝐄𝐑  🐺👮  the destination IP address to filter (or press Enter for all): ")
    duration = input(" 🍬👮  𝐄𝐍𝐓𝐄𝐑  🐺👮  the duration in seconds (or press Enter for continuous sniffing): ")

    if duration:
        duration = int(duration)

    sniff_packets(interface, filter_protocol, filter_port, duration, source_ip, destination_ip)

if __name__ == "__main__":
    start_sniffer()
