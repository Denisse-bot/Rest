from django.urls import path
from profile_api import views

urlpatterns = [
    path('vista/', views.PruebaApiView.as_view())
]
