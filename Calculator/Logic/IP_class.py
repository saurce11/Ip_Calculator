def check_ip_class(ip_address):
    first_octet = int(str(ip_address.split('.')[0]))
    if first_octet <= 127:
        return "A"
    if first_octet <= 191 and first_octet >= 128:
        return "B"
    if first_octet <= 223 and first_octet >= 192:
        return "C"
    if first_octet <= 239 and first_octet >= 224:
        return "D"
    else:
        return "E"
