from django.urls import path
from . import views

urlpatterns = [
    path('', views.SuperTypeList.as_view()),
    path('<int:pk>/', views.SuperTypeDetails.as_view())
]