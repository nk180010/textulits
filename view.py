# i have created this file 
from django import http
from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze  (request):
    djtext=request.POST.get('text','default')
    djremovepunc=request.POST.get('removepunc','off')
    djfullcaps=request.POST.get('fullcaps','off')
    djNewLineRemover=request.POST.get('NewLineRemover','off')
    djSpaceRemover=request.POST.get('SpaceRemover','off')
    djCharCount=request.POST.get('CharCount','off')
    if djremovepunc=="on":
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctations','analyzed_text':analyzed}
        djtext=analyzed
    if djfullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper() 
        params={'purpose':'Changed to upper-case','analyzed_text':analyzed}
        djtext=analyzed
    if djNewLineRemover=="on":
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                 analyzed=analyzed + char
        params={'purpose':'New line remover','analyzed_text':analyzed}
        djtext=analyzed
    # extra space remover
    if djSpaceRemover=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index] ==" " and djtext[index+1]==" "):
                 analyzed=analyzed + char
        params={'purpose':'Space remover','analyzed_text':analyzed}
        djtext=analyzed
    if djCharCount =="on":
        count=len(djtext)
        params={'purpose':'character count','analyzed_text':count}
        djtext=analyzed
    if( djremovepunc !="on" and djSpaceRemover!="on" and djCharCount!="on" and djfullcaps!="on" and djNewLineRemover!="on"):
        return HttpResponse("Error:001")
    return render(request,'analyze.html',params) 
def capfirst(request):
    return HttpResponse("captial first <a href='/'>back</a>")
def newlineremove(request):
    return HttpResponse("new line remove<a href='/'>back</a>")
def spaceremove(request):
    return HttpResponse("space remove <a href='/'>back</a>")
def charcount(request):
    return HttpResponse("character count<a href='/'>back</a>")