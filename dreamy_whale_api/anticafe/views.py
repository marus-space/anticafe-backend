from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class ClientView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response({"clients": serializer.data})

    def post(self, request):
        client = request.data
        serializer = ClientSerializer(data=client)
        if serializer.is_valid(raise_exception=True):
            client_saved = serializer.save()
        return Response({"success": "Client {} created successfully".format(client_saved.last_name + ' ' + client_saved.first_name)})

    def put(self, request, pk):
        saved_client = get_object_or_404(Client.objects.all(), pk=pk)
        data = request.data.get("client")
        serializer = ClientSerializer(instance=saved_client, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            client_saved = serializer.save()
        return Response({"success": "Client {} updated successfully".format(client_saved.last_name + ' ' + client_saved.first_name)})

    def delete(self, request, pk):
        client = get_object_or_404(Client.objects.all(), pk=pk)
        client.delete()
        return Response({
            "message": "Client with ID {} has been deleted.".format(pk)
        }, status=204)
