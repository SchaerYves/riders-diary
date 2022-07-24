from django.urls import path

from . import views

app_name = 'rides'
urlpatterns = [
    # ex: /rides/
    path('', views.index, name='index'),
    # ex: /rides/5/
    path('<int:athlete_id>/', views.detail, name='detail'),
    # ex: /rides/5/results/
    path('<int:athlete_id>/results/', views.results, name='results'),
    # ex: /rides/5/vote/
    path('<int:athlete_id>/vote/', views.vote, name='vote'),
]