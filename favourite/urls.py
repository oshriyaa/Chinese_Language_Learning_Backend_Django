

from django.urls import path
from favourite.views import FavouritePhrase


app_name = 'favourite'
urlpatterns = [
    path('post/<int:phraseID>/', FavouritePhrase.as_view(),name='favourite'),
    # path('get',GetBookmarkView.as_view(),name='getBookmark'),
]