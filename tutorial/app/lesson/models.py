from django.db import models

class Lesson(models.Model): # id kısmını primary-k, incremental olarak kendi yapıyor bişey belirtmezsek
    name = models.CharField(max_length=100) # default null=False'dir ve boş bırakılamaz. null=True boş bırakılabilir
    detail = models.TextField()

    class Meta:
        db_table = "lesson" # db'de tablo lesson_lesson diye oluşuyor, bu sınıf sayesinde sadece lesson olacak

    def __str__(self):
        return self.name