from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('api/watch/', include('watchlist_app.api.urls')),
    path('api/account/', include('user_app.api.urls')),

    # path('api-auth/', include('rest_framework.urls')),
]