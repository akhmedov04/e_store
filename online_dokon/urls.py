from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home2View.as_view()),
    path('main/', include('main.urls')),
    path('user/', include('userapp.urls')),
    path('buyurtma/', include('buyurtma.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
