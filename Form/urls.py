
from django.contrib import admin
from django.db import router
from django.urls import path,include
from .views import index
from app import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('',views.StudentViewSet,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('stuapi',include(router.urls))
]
