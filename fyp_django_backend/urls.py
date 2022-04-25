from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from fyp_django_backend import settings

router = routers.DefaultRouter(trailing_slash=False)
router.register('category', views.Category)

router.register('vocabulary', views.VocabularyView)




urlpatterns = [
path('admin/', admin.site.urls),
path('token/', obtain_auth_token, name='token'),
path('', include(router.urls)),
path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
path(r'^audio/(?P<path>.)$', serve,{'document_root': settings.AUDIO_ROOT}),
path('api/user/', include('users.urls', namespace='users')),
path('Api/Favourites/', include('favourite.urls', namespace='favourites')),
path('api/results/', include('results.urls', namespace='getResults')),



]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.AUDIO_URL, document_root=settings.AUDIO_ROOT)
