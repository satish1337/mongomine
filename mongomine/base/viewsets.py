from rest_framework import viewsets as rest_viewsets
from . import mixins as base_mixins

class BaseGenericViewSet(base_mixins.AnonymousAPIMixin,base_mixins.ActionSerializerAPIMixin,
                         rest_viewsets.GenericViewSet):
    """
    GenericViewSet to be used as Base in Other APIs in application
    Common code required in All APIs can be added here.
    """
