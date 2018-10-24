from .. import models
from . import serializers
from signals.libs.views import APIViewSet

class Person2ViewSet(APIViewSet):
    """
        A class based view for managing Person
    """
    queryset = models.Person2.objects.all()
    serializer_class = serializers.Person2Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

class Company2ViewSet(APIViewSet):
    queryset = models.Company2.objects.all()
    serializer_class = serializers.Company2Serializer

