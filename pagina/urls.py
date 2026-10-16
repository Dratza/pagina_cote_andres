from django.contrib import admin
from django.urls import path
from core import views as core_views
from about import views as about_views
from contact import views as contact_views
from posts import views as posts_views
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name='home'),
    path('about/', about_views.about, name='about'),
    path('contact/', contact_views.contact, name='contact'),
    path('posts/', posts_views.posts, name='posts'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                           document_root = settings.MEDIA_ROOT)