from django.urls import path

from . import views

urlpatterns = [
    #例) /pools/
    path('', views.index, name='index'),
    #例) /pools/5/
    path('<int:question_id>', views.detail, name='detail'),
    #例) /pools/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    #例) /pools/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
