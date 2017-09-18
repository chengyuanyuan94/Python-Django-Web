# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#创建博主基本信息表
class Blogger(models.Model):
	name = models.CharField(max_length=100)
	work = models.CharField(max_length=100)
	tel = models.IntegerField()
	email = models.CharField(max_length=100)

#创建文章信息表
class Content_Table(models.Model):
	content_title = models.CharField(max_length=100)
	content_author = models.CharField(max_length=100)
	content_jianjie = models.TextField()
	content_content = models.TextField()
	content_read = models.IntegerField()
	content_create_date =models.DateTimeField() 
	content_img = models.CharField(max_length=100)
	content_type = models.CharField(max_length=100)