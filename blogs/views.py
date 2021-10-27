from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request,'blogs/blogs.html',context)

def singleblog(request, blog_id):
    single_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blogs/singleblog.html',{'blog':single_blog})