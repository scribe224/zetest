from django.urls import include, path
from rest_framework import routers
from . import views
from .views import RecognitionView
#router = routers.DefaultRouter()
#router.register(r'recognitions', views.RecognitionViewSet)

app_name = "recognitionapi"

urlpatterns = [
    #path('', include(router.urls)),
    #path('recognitions/', RecognitionView.as_view()),
    path('', RecognitionView.as_view())
]