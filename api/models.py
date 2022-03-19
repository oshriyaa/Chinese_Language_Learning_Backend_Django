from operator import mod
from turtle import mode
from django.db import models

# Create your models here.
class Category(models.Model):
    CategoryID = models.CharField(max_length=5, primary_key = True)
    CategoryName = models.CharField(max_length=30)
    class Meta:
        db_table = "category"

class Vocabulary(models.Model):
    WordID = models.AutoField(primary_key = True)
    CategoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    InEnglish = models.CharField(max_length=255)
    InNepali = models.CharField(max_length=255)
    InChinese = models.CharField(max_length = 255)
    InPinYin = models.CharField(max_length=255)
    InDevnagari = models.CharField(max_length=255)
    Audio = models.FileField(upload_to='audio/', blank=True, null=True)
    class Meta:
        db_table = "vocabulary"

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    UserFullName = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=20)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    class Meta:
        db_table = "user"


