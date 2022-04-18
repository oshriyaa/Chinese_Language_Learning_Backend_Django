
from pyexpat import model
from django.contrib import admin

from results import models

# Register your models here.
@admin.register(models.UserResults)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'testDate', 'testTime', 'level', 'result')