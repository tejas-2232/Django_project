"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:

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
from django.urls import path,include
from django.conf.urls import include,url
app_name = 'bgapp'

urlpatterns = [

    path('admin/', admin.site.urls),
    path('bgapp/', include("bgapp.urls"),name='bgapp'),

]


"""
URL_PATTERNS=> parameters
1st is the URL to be searched in the URL bar on the local server and 
2nd is the file you want to run when that URL request is matched, 
the admin is the pre-made application and the file is URL’s file of that app. 
This file is the map of your Django project.
"""