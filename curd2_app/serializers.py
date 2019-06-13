from rest_framework import serializers
from .models import ContactBook,Contact

class ContactBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactBook
        fields='__all__'

class ContactSerializer(serializers.ModelSerializer):
    contact_person=ContactBookSerializer(read_only=True,many=True)
    class Meta:
        model=Contact
        fields='__all__'