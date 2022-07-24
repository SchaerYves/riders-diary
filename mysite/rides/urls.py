from django.urls import path

from . import views

app_name = 'rides'
urlpatterns = [
    # ex: /rides/
    path('', views.index, name='index'),
    # ex: /rides/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /rides/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /rides/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]