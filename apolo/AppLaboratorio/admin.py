from django.contrib import admin
from .models import LabGiratorio, Energia, Abertura

# Register your models here.

admin.site.register(LabGiratorio)
admin.site.register(Energia)
admin.site.register(Abertura)