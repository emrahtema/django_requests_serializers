from django.shortcuts import render
from django.views import View
import requests

from app.lesson.models import Lesson
from django.http import HttpResponse
from app.lesson.helpers import make_requests
from rest_framework.views import APIView
from app.lesson.serializers import LessonSerializer, CustomSerializer
# Create your views here.


class UserView(View):
    def get(self, requests, *args, **kwargs):
        INSERT_DATA = []
        results = make_requests()
        for result in results:
            username = result["login"]["username"]
            street = result["location"]["street"]
            INSERT_DATA.append(
                Lesson(
                    name=username,
                    detail=street
                    )
                )
        Lesson.objects.bulk_create(INSERT_DATA)  # her bir db kaydı için sorgu(insert) oluşturup işliyor
        queryset = Lesson.objects.all()  # dbdeki bütün verileri getir
        serializer = LessonSerializer(queryset, many=True)  # getirilen verileri serializera koy
        return HttpResponse("Created User Data")


class DetailView(APIView):
    def get(self, request, *args, **kwargs):
        id_ = kwargs.get('id')
        try:
            lesson_data = Lesson.objects.filter(
                pk=id_,
            )
        except Lesson.DoesNotExist:
            lesson_data = []

        serializers = LessonSerializer(lesson_data)
        return Response(serializers.data, status=200)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializers_class(data=data)
        if serializer.is_valid():
            data = Lesson.objects.create(**serializer.data)
            return Response(status=200)
        return Response(status=404)


    def delete(self, request, *args, **kwargs):
        delete_id = kwargs.get('id')
        from_data = Lesson.objects.filter(pk=delete_id)
        from_data.delete()
        return Response(status=204)

