from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notes
from .serializers import *

# Create your views here.
@api_view(['GET'])
def notes(req):
    note = Notes.objects.all()
    serialzers = NotesSerializers(note, many=True)
    return Response(serialzers.data)

@api_view(['POST'])
def add_notes(req):
    serializer = NotesSerializers(data=req.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET','PATCH'])
def edit_notes(req, id):
    note = Notes.objects.get(pk=id)

    if req.method == 'GET':
        serializer = NotesSerializers(note)
        return Response(serializer.data)
    
    if req.method == 'PATCH':
        serializer = NotesSerializers(note, data=req.data, partial=True)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(req, id):
    note = Notes.objects.get(pk=id)
    note.delete()

    return Response({"msg":"note deleted"})
