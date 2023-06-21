from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_abilities),
    path('<int:pk>', views.AbilityRetrieveAPIView.as_view()),
    path('create', views.AbilityListCreateAPIView.as_view()),
    path('<int:pk>/delete', views.AbilityDestroyAPIView.as_view()),
    path('<int:pk>/update', views.AbilityUpdateAPIView.as_view())
]