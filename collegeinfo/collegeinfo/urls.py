from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from teacherinfo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Teacher Routes (all from teacherinfo app)
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.logout_view, name="logout"),
=======
from teacherinfo.views import landing,register,registerinfo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/',landing,name='landing'),
    path('register/',register,name='register'),
    path('registerinfo/',registerinfo,name='registerinfo')
>>>>>>> fee0cb37955689d03c653e0254ac5c711a175691
]
