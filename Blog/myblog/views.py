# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from myblog.models import Blogger, Content_Table
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#输出文章内容

# Create your views here.
def index(request):
	#文章数据库
	content_list = Content_Table.objects.all().order_by("-content_create_date")[:5]
	#博主数据库
	blogger_events_list = Blogger.objects.all()	
	return render(request,"index.html",{"events":blogger_events_list ,"content_list":content_list})


def view(request,id = ''):
	blog_content = Content_Table.objects.get(id=id)
	return render(request,"view.html",{"blog":blog_content})

def article(request, page):
    page = int(page)
    pages = [x for x in range(1, get_pages() + 1)]
    end = pages[-1]
    content_list = Content_Table.objects.all()[(page - 1) * 6: page * 6]
    print page
    if get_pages() > 1:
        return render(request, 'article.html', {'content_list': content_list,
                                                          'pages': pages,
                                                          'end': end,
                                                          'page': page,
                                                          'errmsg': 'OK'})
    else:
        return render(request, 'article_.html', {'content_list': content_list,
                                                          'pages': pages,
                                                          'end': end,
                                                          'errmsg': 'faile'})

def get_pages():
    num = divmod(Content_Table.objects.all().count(), 5)
    if num[1] != 0:
        pages = num[0] + 1
    else:
        pages = num[0]
    return pages