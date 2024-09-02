from django.urls import path
from .views import upload_file, delete_file

urlpatterns = [
    path('', upload_file, name="upload-file"),
     path('delete-file/', delete_file, name='delete-file'),
    
]
