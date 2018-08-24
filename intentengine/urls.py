from django.urls import path
from . import views
urlpatterns = [path('',views.login,name='login'),
               path('login/',views.login, name='loginpage'),
               path('enterIntent/',views.enterIntent,name='enterIntent'),
               path('submit/',views.submit, name='submit'),
               path('status/',views.status, name='status')]