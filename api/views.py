from django.shortcuts import render

from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from api.models import Status, Major, Program
from api.serializers import StatusSerialzer, MajorSerialzer, ProgramSerializer

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

class ProgramV(APIView):
    def get(self, request):
        try:
            programs = Program.objects.all()
        except:
            return JsonResponse({"error":"error"}, safe=False)
        serializer = ProgramSerializer(programs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        try:
            major = Major.objects.get(name=request.data['major'])
            status = Status.objects.get(name=request.data['status'])
        except:
            return JsonResponse({"error":"error"}, safe=False)

        Program.objects.create(
            name = request.data['name'],
            text = request.data['text'],
            requirements = request.data['requirements'],
            major = major,
            status = status
        )
        return JsonResponse({"cr": 'eated'}, safe=False)

class ProgramDV(APIView):
    def put(self, request, id):
        try:
            program = Program.objects.get(id=id)
        except:
            return JsonResponse({"asd":"asd"}, safe=False)
        
        
        program.name = request.data['name']
        program.text = request.data['text']
        program.requirements = request.data['requirements']
        program.save()
        return JsonResponse(ProgramSerializer(program).data, safe=False)

    def delete(self, request, id):
        try:
            program = Program.objects.get(id=id)
        except:
            return JsonResponse({"asd":"asd"}, safe=False)
        program.delete()
        return JsonResponse({"gb":"dfg"}, safe=False)