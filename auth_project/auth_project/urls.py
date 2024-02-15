
from django.contrib import admin
from django.urls import path, include
from usuarios.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('home/', home, name='home'),
    path("__reload__/", include("django_browser_reload.urls")),
]
