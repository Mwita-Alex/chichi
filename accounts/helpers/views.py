 from django.shortcuts import render
  def pagenotfound(request, exception):
        return render(request,'accounts/pagenotfound.html')