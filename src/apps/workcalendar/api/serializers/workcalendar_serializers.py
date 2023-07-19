from rest_framework import serializers
from ...models.workcalendar import Workcalendar


class WorkcalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workcalendar
        fields = ['id', 'date', 'holiday']


