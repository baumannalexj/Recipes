from django.contrib import admin
from django.urls import path, include

urlpatterns = [path("", views.hello_world, name="hello_world")]
]
