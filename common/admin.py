from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin.models import LogEntry

admin.site.register(LogEntry)