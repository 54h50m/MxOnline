# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models

# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"城市")
    desc = models.CharField(max_length=200,verbose_name=u"描述")
    add_time = models.DateTimeField(default=datetime.now)


class CourseOrg(models.Model):
    name = models.CharField(max_length=50,verbose_name=u"机构名称")
    desc = models.TextField(verbose_name=u"机构描述")
    click =_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏数")
    image = models.ImageField(upload_to="org/%Y/%m",verbose_name=u"封面图",max_length=100)
    address = models.CharField(max_length=150,verbose_name=u"机构地址")
    city = models.ForeignKey()