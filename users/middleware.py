from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.deprecation import MiddlewareMixin

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Skip authentication for login and register endpoints
        if request.path.startswith('/api/auth/'):
            return None
        
        try:
            auth_header = request.META.get('HTTP_AUTHORIZATION', '').split()
            if len(auth_header) == 2 and auth_header[0].lower() == 'bearer':
                token = auth_header[1]
                JWTAuthentication().authenticate_credentials(token)
        except Exception:
            pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Skip authentication for login and register endpoints
        if request.path.startswith('/api/auth/'):
            return None
            
        try:
            auth_header = request.META.get('HTTP_AUTHORIZATION', '').split()
            if len(auth_header) == 2 and auth_header[0].lower() == 'bearer':
                token = auth_header[1]
                JWTAuthentication().authenticate_credentials(token)
        except Exception:
            pass
