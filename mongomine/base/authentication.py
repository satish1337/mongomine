from django.contrib.auth.models import AnonymousUser
from rest_framework import authentication as rest_authentication

class AnonymousAuthentication(rest_authentication.BaseAuthentication):
    """
    For Views which do not require any authentication.
    """
    def authenticate(self, request):
        """
        Returns AnonymousUser instance and pass as token
        """
        return AnonymousUser(), 'pass'

    def authenticate_header(self, request):
        """
        Returns 'anonymous' to be used
        """
        return 'Anonymous'