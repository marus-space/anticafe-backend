from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import *
from .serializers import *


class ClientView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class SingleClientView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
