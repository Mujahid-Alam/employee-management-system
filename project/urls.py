from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('index/', index),
    path('about/', about),
    path('home/', home),
    path('emp/', include('emp.urls'))

]
