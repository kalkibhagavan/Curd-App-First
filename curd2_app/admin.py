from django.contrib import admin

# Register your models here.
from .models import ContactBook,Contact

class AdminContactBook(admin.ModelAdmin):
    list_display = ['email','mobile','address']

class AdminContact(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Contact,AdminContact)
admin.site.register(ContactBook,AdminContactBook)