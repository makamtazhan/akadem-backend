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

class Manager(serializers.Serializer):
    name = serializers.CharField()

class ProgramSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    text = serializers.CharField()
    requirements = serializers.CharField()
    status = StatusSerialzer()
    major = MajorSerialzer()

