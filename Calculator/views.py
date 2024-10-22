from django.shortcuts import render
import ipaddress
from .forms import IPForm
from .Logic import IP_class
from .Logic import Ip_type


def ip_info(request):
    if request.method == 'POST':
        form = IPForm(request.POST)
        if form.is_valid():
            try:
                raw_ip = form.cleaned_data['ip_address']
                raw_mask = form.cleaned_data['mask']

                # Проверка IP и маски
                my_ip = ipaddress.IPv4Address(raw_ip)
                if not (1 <= int(raw_mask) <= 32):
                    raise ArithmeticError(
                        "Invalid Mask, should be between 1 and 32")

                # Расчет данных сети
                raw_full_address = f"{raw_ip}/{raw_mask}"
                net = ipaddress.IPv4Interface(raw_full_address).network
                my_net = net.network_address
                broadcast_addr = net.broadcast_address
                first_network = my_net + 1
                last_network = broadcast_addr - 1
                next_network = broadcast_addr + 1
                netmask = net.netmask
                hostmask = net.hostmask
                hosts_amount = net.num_addresses
                usable_hosts = max(0, hosts_amount - 2)

                # Формирование контекста для шаблона
                context = {
                    'ip_address': raw_ip,
                    'network_id': net.network_address,
                    'next_network_id': next_network,
                    'prefix': raw_mask,
                    'broadcast_address': broadcast_addr,
                    'netmask': netmask,
                    'hostmask': hostmask,
                    'total_hosts': hosts_amount,
                    'usable_hosts': usable_hosts,
                    'first_host': first_network,
                    'last_host': last_network,
                    'Host_range': f"{first_network} - {last_network}",
                    'ip_type': Ip_type.check_ip_type(my_ip),
                    'ip_class': IP_class.check_ip_class(raw_ip),
                }

                return render(request, 'ip_info.html', context)

            except ipaddress.AddressValueError:
                return render(
                    request, 'ip_info.html', {
                        'error': "Incorrect IP address format"})
            except Exception as e:
                return render(request, 'ip_info.html', {'error': str(e)})

    else:
        form = IPForm()

    return render(request, 'ip_form.html', {'form': form})
