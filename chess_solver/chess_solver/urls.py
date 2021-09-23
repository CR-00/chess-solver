from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('solver.urls'), name='solver'),
    path('admin/', admin.site.urls)
]
