from django.urls import path
from .views import name_list


urlpatterns = [
    path('names/', name_list, name='name_list'),
]
