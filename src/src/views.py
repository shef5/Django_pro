from django.shortcuts import render
from myapp.models import URL, API


# Create your views here.
def about(request):
		return render(request, "about.html", {})

