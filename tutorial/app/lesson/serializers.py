from rest_framework import serializers
from app.lesson.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'  # her şeyi döndüdür. fields = ('name', 'age') felan yapılabilir istenmeyenler için


class CustomSerializer(serializers.Serializer):
    name = serializers.CharField()
    detail = serializers.CharField(required=False)