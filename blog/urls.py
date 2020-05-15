
from django.contrib import admin
from django.urls import path, include
from users.views import UserCreateView 
from .views import api_root
                    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root),
    path('auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('users/', include('users.urls')),
    path('posts/', include('blog_app.urls')),
    path('signup/', UserCreateView.as_view(), name='signup'),
]
