import ipaddress
from Ip_type import check_ip_type
from IP_class import check_ip_class
try:
    raw_ip = input("Enter IP Address: ")
    my_ip = ipaddress.IPv4Address(raw_ip)
    raw_mask = input("Enter Mask in numerical form(1-32): ")
    try:
        if not (1 <= int(raw_mask) <= 32):
            raise ArithmeticError("Invalid Mask, should be between 1 and 32")
    except ValueError:
        raise ValueError("Mask must be in a numerical form")
    raw_full_address = f"{raw_ip}/{raw_mask}"
    net = (ipaddress.IPv4Interface(raw_full_address)).network
    my_net = net.network_address
    broadcast_addr = net.broadcast_address
    next_network = broadcast_addr + 1
    last_network = broadcast_addr - 1
    first_network = my_net + 1
    netmask = net.netmask
    hostmask = net.hostmask
    hosts_amount = net.num_addresses

    usable_hosts = max(0, hosts_amount - 2)
    print(f"Your full  ip address: {raw_full_address}\n"
          f"Your network id: {net}\n"
          f"Usable host range: {first_network} - {last_network}\n"
          f"Your broadcast address: {broadcast_addr}\n"
          f"Your prefix is: {raw_mask}\n"
          f"Netmask: {netmask}\n"
          f"Hostmask: {hostmask}\n"
          f"Your next network id: {next_network}\n"
          f"Your last network id: {last_network}\n"
          f"Your first network id: {first_network}\n"
          f"Total Hosts amount: {hosts_amount}\n"
          f"Usable Hosts: {usable_hosts}\n"
          f"Ip Type: {check_ip_type(my_ip)}\n"
          f"IP Class: {check_ip_class(raw_ip)}")
except ipaddress.AddressValueError:
    print(f"Incorrect Ip address format")
except Exception as e:
    print(e)
