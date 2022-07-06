import hashlib
import json

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import authentication, exceptions


USER_MODEL = get_user_model()


class FrontolTokenAuthentication(authentication.BaseAuthentication):
    """
    Simple token based authentication for Frontol Priority API.

    Clients should authenticate by passing the result of md5 function with
    <access_key> and <request.body> concatenation in the "Authorization"
    HTTP header, prepended with the string "FrontolAuth ".  For example:

        Authorization: FrontolAuth 401f7ac837da42b97f613d789819ff93537bee6a

    """
    keyword = 'FrontolAuth'
    access_key = None
    frontol_user_pk = None

    def get_access_key(self):

        if self.access_key:
            return self.access_key
        return settings.FRONTOL_PRIORITY_API_ACCESS_KEY.encode()

    def get_frontol_user(self):

        pk = self.frontol_user_pk or settings.FRONTOL_PRIORITY_API_USER_PK

        return USER_MODEL.objects.get(pk=pk)

    def authenticate(self, request):

        auth = authentication.get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(request.body, token)

    def authenticate_credentials(self, body, token):

        keybody_hash = hashlib.md5(self.get_access_key() + body).hexdigest()

        if token != keybody_hash:
            raise exceptions.PermissionDenied(_('Invalid token.'))

        user = self.get_frontol_user()

        if not user.is_active:
            raise exceptions.PermissionDenied(_('User inactive or deleted.'))

        return user, None
