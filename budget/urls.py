from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loanview', views.loanview, name='loanview'),
    path('loanview/<int:loan_id>/', views.loanDetail, name='loanDetail'),
    path('addloan', views.addloan, name='addloan'),
    path('loanview/<int:pk>/edit/', views.loanedit, name='loanedit'),
    path('loanview/<int:pk>/delete', views.loandelete, name='loandelete')
]
