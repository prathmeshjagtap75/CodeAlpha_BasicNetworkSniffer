import sys
from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    """
    Callback function that processes each captured network packet.
    Extracts Layer 3 (IP) and Layer 4 (TCP/UDP/ICMP) structural details.
    """
   
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        source_ip = ip_layer.src
        destination_ip = ip_layer.dst
        protocol_num = ip_layer.proto
        
       
        protocol_name = "Unknown"
        if protocol_num == 6:
            protocol_name = "TCP"
        elif protocol_num == 17:
            protocol_name = "UDP"
        elif protocol_num == 1:
            protocol_name = "ICMP"

        print("-" * 60)
        print(f"[+] Packet Captured:")
        print(f"    Source IP:      {source_ip}")
        print(f"    Destination IP: {destination_ip}")
        print(f"    Protocol:       {protocol_name} (Number: {protocol_num})")

       
        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            print(f"    Source Port:    {tcp_layer.sport}")
            print(f"    Dest Port:      {tcp_layer.dport}")
            # If there is raw data payload, display it
            if packet.haslayer('Raw'):
                payload = packet['Raw'].load
                print(f"    Payload (Raw):  {payload[:100]}...") # Shows first 100 bytes

       
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]
            print(f"    Source Port:    {udp_layer.sport}")
            print(f"    Dest Port:      {udp_layer.dport}")
            if packet.haslayer('Raw'):
                payload = packet['Raw'].load
                print(f"    Payload (Raw):  {payload[:100]}...")

       
        elif packet.haslayer(ICMP):
            print(f"    ICMP Type:      {packet[ICMP].type}")

def main():
    print("=" * 60)
    print("             CODEALPHA BASIC NETWORK SNIFFER            ")
    print("=" * 60)
    print("[*] Initializing packet capture loop...")
    print("[*] Sniffing live traffic. Press 'Ctrl + C' to terminate safely.\n")
    
    try:
        
        sniff(prn=packet_callback, store=0)
    except PermissionError:
        print("\n[!] ERROR: Insufficient privileges. You MUST run this script as an Administrator / Root user.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[-] Sniffer halted successfully. Exiting clean.")
        sys.exit(0)

if __name__ == "__main__":
    main()