from django.urls import include,path
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from groceries import views

router = routers.DefaultRouter()
router.register(r'food', views.FoodViewSet)

urlpatterns = [
    path('', include(router.urls))
]