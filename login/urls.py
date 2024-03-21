from login import views
from django.urls import path

urlpatterns = [

    path('login/',views.login),
    path('registered/',views.registered),
    path('vification/',views.verification),

]