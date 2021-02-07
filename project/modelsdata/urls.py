from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('tarrifs/', views.tarrifsPage, name='tarrifs'),
    path('model/<slug>', views.ModelsDataDetailPage.as_view(), name='model-detail'),
    path('model/<slug>/<request_slug>', views.PredictionrequestDetailPage.as_view(), name='request-detail'),
]