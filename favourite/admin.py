from pyexpat import model
from django.contrib import admin

from favourite import models

# Register your models here.
@admin.register(models.Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'vocabulary')