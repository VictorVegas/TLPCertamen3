from django.urls import path
from . import views

urlpatterns = [
    path("eventos/", views.EventoList.as_view(), name="eventos"),
    path("evento/<int:pk>/", views.EventoDetail.as_view()),
    path("tipos/", views.TipoEventoList.as_view()),
    path("tipos/<int:pk>/", views.TipoEventoDetail.as_view()),
    path('holidays/<int:year>/', views.getHolidays, name='holidays'),
]
