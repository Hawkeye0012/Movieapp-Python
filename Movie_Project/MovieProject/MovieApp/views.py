from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movies
from .form import MovieForm


# Create your views here.

def hello(request):
    movies = Movies.objects.all()
    context = {
        'movie_list': movies
    }
    return render(request, 'index.html', context)


def details(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie})


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('description')
        image = request.FILES['img']
        year = request.POST.get('year')
        movie = Movies(name=name, description=desc, img=image, year=year)
        movie.save()

    return render(request, 'add.html')


def update(request, id):
    movie = Movies.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    # here we're getting the values that inputted as 'request.POST' forms or other forms(i.e.None)
    # and 'FILE' forms. instance means the table name
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == "POST":
        movie = Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
