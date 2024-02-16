
from django.contrib import admin
from django.urls import path,include
from login import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    # path()
    path('', views.index), 
    path('allotment/',include('allotment.urls')),
]
