from django.contrib import admin

# Register your models here.
from  .models import * #importamos el archivo models

admin.site.register(Autor)
