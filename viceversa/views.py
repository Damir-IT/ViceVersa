from django.shortcuts import render

def viceversa(request):
    return render(request, 'viceversa.html')

def reverse(request):
    return render(request, 'reverse.html')
