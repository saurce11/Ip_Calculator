def check_ip_type(my_ip):
    if my_ip.is_loopback:
        return "Loopback"
    if my_ip.is_link_local:
        return "Link-local"
    if my_ip.is_global:
        return "Global"
    if my_ip.is_private:
        return "Private"
    else:
        return "Unknown"
