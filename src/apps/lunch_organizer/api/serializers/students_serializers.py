from rest_framework import serializers
from ...models.student import Student
from ...models.classroom import Classroom


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'scholar_year', 'name', 'surname', 'allergies', 'classroom']

    def to_representation(self, instance):
        representation = super().to_representation(instance=instance)
        classroom_id = representation['classroom']
        classroom = Classroom.objects.filter(id=classroom_id).first()
        representation['classroom'] = str(classroom)
        return representation


class StudentScholarYear(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['scholar_year']
