from django.urls import include, path

from users.views import CustomUserCreate


app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),

]

