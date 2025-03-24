from django.shortcuts import render

def sample(request):
    return render(request, 'sample.html')  # Make sure this template exists