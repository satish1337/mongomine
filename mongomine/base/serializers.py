from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongo_serializer
from . import mixins as base_mixins


class BaseModelSerializer(base_mixins.CustomResponseSerializerMixin, serializers.ModelSerializer):
    """
    Serializer to be used as Base in Other Model serializers in application
    Common code required in All Serializers can be added here or
    In separate mixins and then inherited here
    It also extends from CustomResponseSerializerMixin which re-formats the data as required
    """

class BaseAPISerializer(base_mixins.CustomResponseSerializerMixin, serializers.Serializer):
    """
    Serializer to be used as Base in Other serializers in application
    Common code required in All Serializers can be added here or
    In separate mixins and then inherited here
    It also extends from CustomResponseSerializerMixin which re-formats the data as required
    """

class BaseMongoSerializer(base_mixins.CustomResponseSerializerMixin, mongo_serializer.DocumentSerializer):
    """
    Serializer to be used as Base in Other Model serializers in application
    Common code required in All Serializers can be added here or
    In separate mixins and then inherited here
    It also extends from CustomResponseSerializerMixin which re-formats the data as required
    """
    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def _get_default_field_names(self, *args, **kwargs):
        return self.get_field_names(*args, **kwargs)


class CustomMessageSerializer(BaseAPISerializer):
    """
    serializer to pass custom message in response
    """
    custom_message = ""

    def __init__(self, *args, **kwargs):
        custom_message = kwargs.pop('custom_message', '')
        self.custom_message = custom_message
        super(CustomMessageSerializer, self).__init__(*args, **kwargs)

    @property
    def data(self):
        # If any child serializer needs to override the data method,
        # it should first call the super class data
        message_dict = {
            "message": self.custom_message
        }
        data = super(CustomMessageSerializer, self).data
        data.update(message_dict)
        return data

