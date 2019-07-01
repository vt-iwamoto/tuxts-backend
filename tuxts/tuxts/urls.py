from django.urls import include, path
from rest_framework import routers
from backend import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'texts', views.TextViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
