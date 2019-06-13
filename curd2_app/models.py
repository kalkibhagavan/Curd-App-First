from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ContactBook(models.Model):
    contact=models.ForeignKey(Contact,on_delete=models.CASCADE,related_name='contact_person')
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    address=models.TextField(max_length=1000)

    def __str__(self):
        return self.email
