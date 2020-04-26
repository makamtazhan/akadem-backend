from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from api.serializers import StatusSerialzer, MajorSerialzer
from api.models import Status, Major

@api_view(['GET'])
def statuses(request):
    try:
        status = Status.objects.all()
    except:
        return JsonResponse({"error":"error"}, safe=False)
    serializer = StatusSerialzer(status, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def majors(request):
    try:
        majors = Major.objects.all()
    except:
        return JsonResponse({"error":"error"}, safe=False)
    serializer = MajorSerialzer(majors, many=True)
    return JsonResponse(serializer.data, safe=False)
