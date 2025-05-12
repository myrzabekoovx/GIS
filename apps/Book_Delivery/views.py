from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.Book_Delivery.models import Delivery, Process
from apps.Book_Delivery.serializers import DeliverySerializer, ProcessSerializer


@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})


class DeliveryList(APIView):
    def get(self, request):
        deliveries = Delivery.objects.all()
        serializer = DeliverySerializer(deliveries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeliverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProcessDetailApiView(APIView):
    def get_object(self, pk):
        try:
            return Process.objects.get(pk=pk)
        except Process.DoesNotExist:
            return None

    def get(self, request, pk):
        process = self.get_object(pk)
        if process is None:
            return Response(
                {"error": "Process not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = ProcessSerializer(process)
        return Response(serializer.data)

    def put(self, request, pk):
        process = self.get_object(pk)
        if process is None:
            return Response(
                {"error": "Process not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = ProcessSerializer(process, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        process = self.get_object(pk)
        if process is None:
            return Response(
                {"error": "Process not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        process.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)