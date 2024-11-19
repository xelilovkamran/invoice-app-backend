from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from drf_social_oauth2.authentication import SocialAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class MultiAuthentication(BaseAuthentication):
    def __init__(self):
        self.oauth2_auth = OAuth2Authentication()
        self.social_auth = SocialAuthentication()
        self.jwt_auth = JWTAuthentication()

    def authenticate(self, request):
        # JWT
        try:
            return self.jwt_auth.authenticate(request)
        except AuthenticationFailed:
            pass

        # OAuth2
        try:
            return self.oauth2_auth.authenticate(request)
        except AuthenticationFailed:
            pass

        # Social Auth
        try:
            return self.social_auth.authenticate(request)
        except AuthenticationFailed:
            pass

        return None
