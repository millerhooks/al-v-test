from rest_framework import serializers
from threat import IPDetails

# DRF Field type listing - jn
# http://www.django-rest-framework.org/api-guide/fields#field


class DetailsSerializer(serializers.Serializer):
    is_valid = serializers.Field()
    # serialize your values in IPDetails here
    # use serializers.Field()