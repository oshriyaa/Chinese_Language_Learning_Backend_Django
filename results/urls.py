from django.urls import path

from results.views import UserResultsData, GetResultsView
# from results.views import UserResultsData


app_name = 'results'
urlpatterns = [
    path('post/', UserResultsData.as_view(),name='createResults'),
    path('get/', GetResultsView.as_view(),name='getResults'),
]