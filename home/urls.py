from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',homefn),
    path('view/<int:s_id>',viewfn),
    path('link/',link),
    path('category/<int:c_id>',catfn),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)