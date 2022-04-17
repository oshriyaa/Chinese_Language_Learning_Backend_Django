

from django.urls import path
from favourite.views import FavouritePhrase, GetFavouriteView


app_name = 'favourite'
urlpatterns = [
    path('post/<int:WordID>/', FavouritePhrase.as_view(),name='favourite'),
    path('get/',GetFavouriteView.as_view(),name='getFavourites'),
]