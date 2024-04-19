from django.conf import settings
from django.http import HttpResponseForbidden

class BlockMaliciousIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the client's IP address from the request
        client_ip = request.META.get('REMOTE_ADDR')
        print(client_ip);
        # Check if the IP is in the list of malicious IPs
        if self.is_malicious_ip(client_ip):
            # If it's malicious, block the request
            return HttpResponseForbidden("Your IP address is blocked.")
        else:
            # If not, continue with the request
            response = self.get_response(request)
            return response

    def is_malicious_ip(self, ip):
        # Access the list of malicious IPs from settings
        malicious_ips = getattr(settings, 'MALICIOUS_IPS', [])
        return ip in malicious_ips
