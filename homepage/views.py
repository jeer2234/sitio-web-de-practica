from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import NameForm


# Create your views here.



def about(request):
    
    return render(request,'homepage/about.html',)


def index(request):
    return render(request,'homepage/index.html',)


def register(request):
    """The login page for condimentos."""
    return render(request,'homepage/register.html')

def contact(request):
    """The login page for condimentos."""
    return render(request,'homepage/contact.html')

def login(request):
    """The login page for condimentos."""
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request,'homepage/login.html', {'form': form})

def services(request):
    """The login page for condimentos."""
    return render(request,'homepage/services.html')