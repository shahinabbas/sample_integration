from django.urls import path
from .views import your_api_view

urlpatterns = [
    path('send_file/', your_api_view, name='send_file_api'),
]
