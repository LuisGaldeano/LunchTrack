from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ...api.serializers.students_serializers import StudentsSerializer, StudentListSerializer, StudentScholarYear
from ...models.student import Student


@api_view(['GET', 'POST'])
def student_api_view(request):
    if request.method == 'GET':
        students = Student.objects.all()
        students_serializer = StudentListSerializer(students, many=True)
        return Response(students_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        student_serializer = StudentsSerializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data, status=status.HTTP_201_CREATED)
        return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_api_view(request, pk=None):
    student = Student.objects.filter(id=pk).first()
    if student:
        if request.method == 'GET':
            student_serializer = StudentsSerializer(student)
            return Response(student_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            student_serializer = StudentsSerializer(student, data=request.data)
            if student_serializer.is_valid():
                student_serializer.save()
                return Response(student_serializer.data, status=status.HTTP_200_OK)
            return Response(student_serializer.data, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            student.delete()
            return Response({'message': 'student deleted correctly'}, status=status.HTTP_200_OK)

    return Response({'message': 'Student not found'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def student_scholar_year(request):
    if request.method == 'GET':
        students = Student.objects.first()
        students_serializer = StudentScholarYear(students, many=False)
        return Response(students_serializer.data, status=status.HTTP_200_OK)
