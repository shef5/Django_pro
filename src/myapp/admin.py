from django.contrib import admin

# Register your models here.
from .forms import URLform
from .models import URL, API

class Inputurl(admin.ModelAdmin):
	list_display = ["__str__", "timestamp", "updated"]
	class Meta:
		model = URL

class Inputurl1(admin.ModelAdmin):
	list_display = ["__str__", "nofollow" , "timestamp", "updated"]
	class Meta:
		model = API

admin.site.register(URL, Inputurl)
admin.site.register(API, Inputurl1)