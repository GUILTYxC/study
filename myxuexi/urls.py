

from django.urls import path,include

urlpatterns = [

    path('index/', include('myapp.urls')),

    path('myadmin/', include('myadmin.urls')),

    path('mybei/', include('mybei.urls')),



]
