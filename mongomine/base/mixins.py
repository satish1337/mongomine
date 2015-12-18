from rest_framework import permissions as rest_permissions


class AnonymousAPIMixin(object):
    """
    This mixin contains all common functionality required in throughout the APIs
    """
    anonymous_allowed_actions = ()

    def get_permissions(self):
        # Allow any if action is one of anonymous_allowed_actions
        return (
            [rest_permissions.AllowAny()] if self.action in self.anonymous_allowed_actions else
            super(AnonymousAPIMixin, self).get_permissions()
        )

    def initialize_request(self, request, *args, **kargs):
        """
        Set authenticators (or authentication_classes) to
        AnonymousAuthentication if action is one of anonymous_allowed_actions
        """
        from . import authentication as common_authentication

        result = super(AnonymousAPIMixin, self).initialize_request(request, *args, **kargs)
        if self.action in self.anonymous_allowed_actions:
            result.authenticators = [common_authentication.AnonymousAuthentication()]
        return result



class CustomResponseSerializerMixin(object):
    """
    Mixin to format serializer data to a custom response
    All serializers to inherit from this
    """
    @property
    def data(self):
        # If any child serializer needs to override the data method,
        # it should first call the super class data
        data = super(CustomResponseSerializerMixin, self).data
        return {
            'data': data
        }


class ActionSerializerAPIMixin(object):
    """
    This mixin is used to add provision for using a different serializer for every action of an API
    Add this mixin and define <action>_serializer_class attribute in API, which will used for respective <action>
    """
    def get_serializer_class(self):
        return getattr(self, '{0}_serializer_class'.format(self.action.lower())) if \
            self.action and getattr(self, '{0}_serializer_class'.format(self.action.lower()), None) \
            else super(ActionSerializerAPIMixin, self).get_serializer_class()