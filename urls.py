
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('student_Regform.urls')),
    path('admin/', admin.site.urls),
]
