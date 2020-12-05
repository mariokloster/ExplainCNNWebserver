from django.shortcuts import render


# Create your views here.

def startpage(request):
    return render(request, 'startpage.html', {})

def about(request):
    return render(request, "About.html", {})
