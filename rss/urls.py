from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [
    path("", views.index, name='index'),
    path("news", views.news, name='news'),
    path('', include(router.urls)),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]