from django.urls import path
from app.lesson import views

urlpatterns = [
    path("create_user/", views.UserView.as_view(), name="createuser"),
    path("detail_user/<int:id>", views.DetailView.as_view(), name="detailuser")
]
