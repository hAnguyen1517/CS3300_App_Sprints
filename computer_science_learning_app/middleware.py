from django.http import HttpResponseForbidden

class BlockMaliciousIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

# Get the client's IP address from the request
    def __call__(self, request):
        client_ip = request.META.get('REMOTE_ADDR')

        # Check if the IP is in the list of malicious IPs
        if self.is_malicious_ip(client_ip):
            # If it's malicious, block the request
            return HttpResponseForbidden("Your IP address is blocked.")
        else:
            # If not, continue with the request
            response = self.get_response(request)
            return response

    def is_malicious_ip(self, ip):
        # Implement your logic to check if the IP is malicious
        malicious_ips = ['192.168.56.1', '10.20.15.245']  # Example list of malicious IPs
        return ip in malicious_ips
