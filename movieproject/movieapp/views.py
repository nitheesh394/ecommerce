from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import form


# Create your views here.
def new(request):
    movies = movie.objects.all()
    content = {'name': movies}
    return render(request, 'index.html', content)


def detail(request, movie_id):
    m = movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movies': m})


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name', )

        desc = request.POST.get('desc', )

        year = request.POST.get('year', )

        img = request.FILES['img']
        movies = movie(name=name, desc=desc, year=year, img=img)
        movies.save()

    return render(request, 'add.html')


def update(request, id):
    movies = movie.objects.get(id=id)
    forms = form(request.POST or None, request.FILES, instance=movies)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request, 'edit.html', {'forms': forms, 'movies': movies})


def delete(request, id):
    if request.method == 'POST':
        movies = movie.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request, 'delete.html')


