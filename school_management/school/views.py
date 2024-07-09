from rest_framework import viewsets
from .models import User, Subject, Mark
from .serializers import UserSerializer, SubjectSerializer, MarkSerializer
#from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
   # permission_classes = [IsAuthenticated]


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    #permission_classes = [IsAuthenticated]


class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    #permission_classes = [IsAuthenticated]
