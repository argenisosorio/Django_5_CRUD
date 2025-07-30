from django.shortcuts import render

def home(request):
    context = {
        'message': '¡Hello Django 5!',
    }

    return render(request, 'myapp/home.html', context)
