from django.urls import include, path
from django.conf import settings
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
      path('', views.index),
      path('sensors/<int:id>', views.sensor_page),

      path('profile/', include('social_django.urls', namespace='social')),
      path('profile/logout/',  LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},
           name='logout'),
      path('profile/secure/', views.secure, name='secure'),

      path('api/sensors', views.SensorsAPIView.as_view()),
      path('api/sensors/<int:id>/', views.SensorAPIView.as_view()),
      path('api/sensors/<int:id>/measurement', views.SensorMeasurementAPIView.as_view()),
      path('api/files/csv', views.FilesAPIView.as_view()),

]
