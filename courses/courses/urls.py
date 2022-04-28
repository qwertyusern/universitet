from django.contrib import admin
from django.urls import path
from kurslar.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', asosiy),
    path('ustoz/', ustoz),
    path('fan/', fan),
    path('yonalish/', yonalish),
]

