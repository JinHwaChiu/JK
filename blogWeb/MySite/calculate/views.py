# coding: utf-8 
# from __future__ import unicode_literals

from django.shortcuts import render

#它是用来向网页返回内容的，就像Python中的 print 一样，只不过 HttpResponse 是把内容显示到网页上。
from django.http import HttpResponse

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))
   
def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
    
#注：request.GET 类似于一个字典，更好的办法是用 request.GET.get('a', 0) 当没有传递 a 的时候默认 a 为 0


def home(request):
   string = u'fighting加油'
   return render(request,'calculate/home.html',{'string':string})

def tutorial(request):
   tutorial =['1','2','3','4']
   return render(request,'calculate/home.html',{'tutorial':tutorial})

def info_dic(request):
   info_dic = {'site':u'fight','content':u'ITIT'}
   return render(request,'calculate/home.html',{'info_dic':info_dic})
def Map(request):
   List = map(str,range(100))
   #return HttpResponse(List)
   return render(request,'calculate/home.html',{'List':List})
   
def bootstrap(request):
   return render(request,'calculate/boot.html')
   
   
   
   
   
   
   
   