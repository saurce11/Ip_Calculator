from django.db import models

# Create your models here.
class IPAddressData(models.Model):
    ip_address = models.CharField(max_length=15)
    network_id = models.CharField(max_length=15)
    broadcast_address = models.CharField(max_length=15)
    prefix = models.CharField(max_length=15)
    netmask = models.CharField(max_length=15)
    hostmask = models.CharField(max_length=15)
    next_network_id = models.CharField(max_length=15)
    first_network_id = models.CharField(max_length=15)
    last_network_id = models.CharField(max_length=15)
    host_range = models.CharField(max_length=15)
    total_hosts = models.CharField(max_length=15)
    usable_hosts = models.IntegerField()
    ip_type = models.CharField(max_length=20)
    ip_class = models.CharField(max_length=1)

    def __str__(self):
        return self.ip_address
