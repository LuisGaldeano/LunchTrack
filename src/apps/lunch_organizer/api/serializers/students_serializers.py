from rest_framework import serializers
from ...models.student import Student
from ...models.classroom import Classroom


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance=instance)
        classroom_id = representation['classroom']
        classroom = Classroom.objects.filter(id=classroom_id).first()
        representation['classroom'] = str(classroom)
        return representation

    # {
    #     "name": "Jaime Paco",
    #     "surname": "Martin",
    #     "allergies": "",
    #     "classroom": 1
    # }
