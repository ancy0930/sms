from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SubjectViewSet, MarkViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"subjects", SubjectViewSet)
router.register(r"marks", MarkViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('token/',obtain_auth_token,name="login"),
]
