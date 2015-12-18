from base import viewsets as base_viewsets
from . import serializers as mongoengine_serializers
from . import models as mongoengine_models

from rest_framework import mixins as rest_mixins


class CandidateViewSet(rest_mixins.ListModelMixin, base_viewsets.BaseGenericViewSet):
    """
    This viewset is used for operations on **candidate** model.
    """

    serializer_class = mongoengine_serializers.CandidateSerializer
    model = mongoengine_models.Candidate
    queryset = model.objects.all()