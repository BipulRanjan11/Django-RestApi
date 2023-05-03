from django.urls import path, include
from rest_framework import routers

from .views import WorkList, RegistrationView,ArtistViewSet

router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)

urlpatterns = [
    path('api/works/', WorkList.as_view(), name='work-list'),
    path('api/register/', RegistrationView.as_view(), name='registration'),
    path('api/', include(router.urls)),
]
