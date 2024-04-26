from django.conf import settings
from django.http import HttpResponseForbidden

# Defines a middleware class to handle blocking of malicious IP addresses
class BlockMaliciousIPMiddleware:
    # Constructor method for the middleware class
    def __init__(self, get_response):
        # Initializes the middleware with a function to get the response
        self.get_response = get_response

    # Get the client's IP address from the request
    def __call__(self, request):
        # Passing the request to the next middleware or view function
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
    # Method to check if an IP address is malicious
    def is_malicious_ip(self, ip):
        # Access the list of malicious IPs from settings
        malicious_ips = getattr(settings, 'MALICIOUS_IPS', [])
        # Check if the provided IP is in the list of malicious IPs
        return ip in malicious_ips
