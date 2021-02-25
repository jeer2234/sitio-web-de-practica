from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def renderizar(request):
    context = {}
    
    return HttpResponse("Hello, world. You're at the polls index.")
    
def visualizar(request):
    return render(request,'homepage/index.html',{})