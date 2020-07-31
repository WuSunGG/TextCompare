from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('v2', views.index2, name='index2'),
    path('v2/<int:distance>', views.index21, name='index2'),
    path('v2/compare/<slug:fp>/<slug:tp>', views.compare),
    path('v3/<int:distance>', views.index3, name='index3'),
    path('v1/html', views.htmlcheckv1, name='htmlcheckv1'),
]