from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def index(request,value1, value2):
    return render(request, "infordetails.html", {"data": value1+value2})