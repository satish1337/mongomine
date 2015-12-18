from . import models as mongoengine_models
from base import serializers as base_serializers


class CandidateSerializer(base_serializers.BaseMongoSerializer):
    class Meta:
        model = mongoengine_models.Candidate