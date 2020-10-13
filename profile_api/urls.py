from django.urls import path
from profile_api import views

urlpatterns = [
    path('vista/', views.PruebaApiview.as_view()),
]
