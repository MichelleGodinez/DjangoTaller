from django.contrib import admin
from .models import InfoGeneral

class InfoGeneralAdmin(admin.ModelAdmin):
	pass

admin.site.register(InfoGeneral,InfoGeneralAdmin)
# Register your models here.
