from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Cliente)
admin.site.register(models.Sucursal)
admin.site.register(models.Auto)