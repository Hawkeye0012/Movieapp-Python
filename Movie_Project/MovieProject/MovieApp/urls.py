from django.urls import path
from MovieApp import views

app_name = 'MovieApp'
urlpatterns = [
    path('', views.hello, name='hello'),
    path('movie/<int:movie_id>/', views.details, name='details'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')

]
