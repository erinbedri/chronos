from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('chronos.web.urls', 'chronos.web.urls'), namespace='web')),
    path('accounts/', include(('chronos.accounts.urls', 'chronos.accounts.urls'), namespace='accounts')),
    path('posts/', include(('chronos.posts.urls', 'chronos.posts.urls'), namespace='posts')),
    path('watches/', include(('chronos.watches.urls', 'chronos.watches.urls'), namespace='watches')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
