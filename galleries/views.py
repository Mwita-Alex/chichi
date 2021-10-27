from django.shortcuts import render
from .models import Gallery

# Create your views here.
def gallery(request):
    images = Gallery.objects.all()
    context = {'images' : images}
    return render(request,'galleries/pictures.html',context)