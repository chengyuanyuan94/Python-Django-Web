# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myblog.models import Blogger , Content_Table

#博主信息表
class BolggerAdmin(admin.ModelAdmin):
	list_display = ['name','work','tel','email']
admin.site.register(Blogger,BolggerAdmin)

#文章表
class Content_TableAdmin(admin.ModelAdmin):
	list_display = ['id','content_title','content_author','content_jianjie','content_content','content_create_date','content_img','content_type']
admin.site.register(Content_Table,Content_TableAdmin)

# Register your models here.
