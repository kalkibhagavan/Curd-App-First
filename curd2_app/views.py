from django.shortcuts import render

# Create your views here.
from .models import Contact,ContactBook
from .serializers import ContactSerializer,ContactBookSerializer
from rest_framework import generics

class ContactListView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactBookListView(generics.ListCreateAPIView):
    queryset = ContactBook.objects.all()
    serializer_class = ContactBookSerializer

class ContactBookDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactBook.objects.all()
    serializer_class = ContactBookSerializer