from django.shortcuts import render

from .forms import *
from .models import *

# Create your views here.


def home(request):

    form = OrdonnanceForm()
    if request.method == "POST":
        form = OrdonnanceForm(request.POST)

        if form.is_valid():            
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'convertion/index.html', context)