from django.contrib import admin
from django.urls import path, include,re_path
from nive import views as v1
appname='nive'
urlpatterns = [
    # path('admin/', admin.site.urls),
  
    path('sample/',v1.sample),
    path('form/', v1.form),
    path('create/', v1.create_data),
    ]
