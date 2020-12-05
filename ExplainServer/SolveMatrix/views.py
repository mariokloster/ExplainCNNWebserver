from django.shortcuts import render, redirect
from .forms import Matrix


# Create your views here.
def inputMatrix(request):
    form = Matrix()
    return render(request, "inputMatrix.html", {'matrix': form})
