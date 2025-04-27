from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('search', views.search, name='search'),
    path('filter', views.filter, name='filter'),
    path('report', views.report, name='report'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/destroy/', views.destroy, name='destroy'),
]
