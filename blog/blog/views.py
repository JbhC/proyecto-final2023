from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

# def posts(request):
#     return render(request, 'posts.html')
