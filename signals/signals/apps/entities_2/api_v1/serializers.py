from rest_framework import serializers
from ..models import Person2, Company2
from signals.libs.serializers import AuditedModelSerializer
from signals.apps.authentication.api_v1.serializers import UserSerializer

class PersonSerializerAdmin(AuditedModelSerializer):
    class Meta:
        model = Person2
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
