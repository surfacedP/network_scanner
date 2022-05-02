import scapy.all as scapy
import click


@click.command()
@click.option("-i", "--ip", prompt="Input IP range", help="IP range to scan")
def start(ip):
    ip = ip.encode("utf-8") # Encode IP - scapy fails to scan unicode
    scan_result = scan(ip)
    print_result(scan_result)


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for client in answered_list:
        client_dict = {"ip": client[1].psrc, "mac": client[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\t      MAC Address\n-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


if __name__ == "__main__":
    start()
