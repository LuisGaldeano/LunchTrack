from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..serializers.classroom_serializers import ClassroomSerializer
from ...models import Classroom


@api_view(['GET', 'POST'])
def classroom_api_view(request):
    if request.method == 'GET':
        classroom = Classroom.objects.all()
        classroom_serializer = ClassroomSerializer(classroom, many=True)
        return Response(classroom_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        classroom_serializer = ClassroomSerializer(data=request.data)
        if classroom_serializer.is_valid():
            classroom_serializer.save()
            return Response(classroom_serializer.data, status=status.HTTP_201_CREATED)
        return Response(classroom_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def classroom_detail_api_view(request, pk=None):
    classroom = Classroom.objects.filter(id=pk).first()
    if classroom:
        if request.method == 'GET':
            classroom_serializer = ClassroomSerializer(classroom)
            return Response(classroom_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            classroom_serializer = ClassroomSerializer(classroom, data=request.data)
            if classroom_serializer.is_valid():
                classroom_serializer.save()
                return Response(classroom_serializer.data, status=status.HTTP_200_OK)
            return Response(classroom_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            classroom.delete()
            return Response({'message': 'Classroom deleted correctly'}, status=status.HTTP_200_OK)

    return Response({'message': 'Classroom not found'}, status=status.HTTP_400_BAD_REQUEST)
