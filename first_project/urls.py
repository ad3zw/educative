"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from first_app import views
from django.urls import include


urlpatterns = [
    path('', include('first_app.urls')),
    #path('<age>/', views.show_age, name='show_age'),
    path('admin/', admin.site.urls),
     #the default url will call views.index of the first_app app.
    #Here we have mapped the default url to the first_app views file and called the index function.
    #The 3rd parameter name='index' specifies we are naming the url '' to be index.
]
