from extras.reports import Report
from ipam.models import IPAddress

# Report for all NATted IP addresses


class NATIPReport(Report):
    description = "List all natted IP addresses"

    def test_natted_ip(self):
        for ip in IPAddress.objects.filter(nat_inside__isnull=False):
            self.log_success(ip, "NAT IP address for private IP: {} Description: {}".format(
                ip.nat_inside.address, ip.description))
