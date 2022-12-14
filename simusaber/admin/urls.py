"""admin URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import path
from django.conf.urls import include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('accounts/login/',LoginView.as_view(template_name="general/login.html"), name="login"),
    # path('accounts/logout/',logout_then_login, name="logout"),
    path('profiles/', include(('apps.profiles.urls', 'profiles'), namespace="profiles")),
    path('locations/', include(('apps.locations.urls', 'locations'), namespace="locations")),
]


