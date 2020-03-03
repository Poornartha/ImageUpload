from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
# Create your views here.


def hotel_image_view(request):
    form = HotelForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            form = HotelForm()
    return render(request, 'image_app/reister.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
