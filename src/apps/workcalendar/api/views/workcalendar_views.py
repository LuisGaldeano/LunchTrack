from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ...models.workcalendar import Workcalendar
from datetime import date, timedelta
from django.db import transaction
from workalendar.europe import Spain
from ..serializers.workcalendar_serializers import WorkcalendarSerializer


@api_view(['GET', 'POST'])
def workcalendar_api_view(request):
    if request.method == 'GET':
        calendar = Workcalendar.objects.all()
        calendar_serializer = WorkcalendarSerializer(calendar, many=True)
        return Response(calendar_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        calendar_serializer = WorkcalendarSerializer(data=request.data)
        if calendar_serializer.is_valid():
            dates = request.data.get('date')
            holiday = request.data.get('holiday')

            Workcalendar.objects.create(date=dates, holiday=holiday)
            return Response(calendar_serializer.data, status=status.HTTP_201_CREATED)
        return Response(calendar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def workcalendar_download_api_view(request):
    spain = Spain()
    year = 2023
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    delta = timedelta(days=1)

    with transaction.atomic():
        current_date = start_date
        while current_date <= end_date:
            is_holiday = spain.is_holiday(current_date)
            is_weekend = current_date.weekday() >= 5

            Workcalendar.objects.get_or_create(date=current_date, holiday=is_holiday or is_weekend)
            current_date += delta

    calendar = Workcalendar.objects.all()
    calendar_serializer = WorkcalendarSerializer(calendar, many=True)
    return Response(calendar_serializer.data, status=status.HTTP_200_OK)
