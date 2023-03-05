from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from rooms.views import RoomViewSet, BookingViewSet

room_router = routers.SimpleRouter()
room_router.register("rooms", RoomViewSet, basename="rooms")

booking_router = routers.SimpleRouter()
booking_router.register("booking", BookingViewSet, basename="booking")

urlpatterns = [
    path('', include(room_router.urls)),
    path('', include(booking_router.urls)),
    path('users/', include('users.urls')),

    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
