from django.contrib import admin
from django.urls import path
from teacherinfo import views
from teacherinfo.views import landing, register, registerinfo

urlpatterns = [
    path('admin/', admin.site.urls),

    # Teacher Routes (all from teacherinfo app)
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.logout_view, name="logout"),

    # Additional routes
    path('', landing, name='landing'),
    path('registerinfo/', registerinfo, name='registerinfo'),
]