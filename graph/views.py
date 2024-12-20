from django.shortcuts import render


def index(request):
    context = {
        'text': 'Real-Time Graph'
    }

    return render(request, 'index.html', context)
