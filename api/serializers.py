from rest_framework import serializers
from api.models import Status, Major
class StatusSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = 'id', 'name'

class MajorSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = 'id', 'name'