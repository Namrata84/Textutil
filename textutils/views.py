#I have create this file - Namu
#video 6
from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
#    return HttpResponse('''<h1>Harry</h1> <a href="http://www.facebook.com">Facebook</a>''')

#def about(request):
#    return HttpResponse("About Harry Bhai")

#video 7
def index(request):
    #return HttpResponse("Home")
    #params = {'name': 'harry', 'place': 'Mars'}
    return render(request, 'index.html')

# def removepunc(request):
#     #Get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     #Analyze the text
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove")
#
# def spaceremove(request):
#     return HttpResponse("space remove <a href='/'>back<a/>")
#
# def charcount(request):
#     return HttpResponse("char count")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Chack checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    exstraspaceremover = request.POST.get('exstraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc =="on":
         punctuations = '''!()-[]{}:;'"\,<>.@%$&*_~'''
         analyzed = ""
         for char in djtext:
             if char not in punctuations:
                 analyzed = analyzed + char

         params = {'purpose':'Removed space remover', 'analyzed_text': analyzed}
         djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (exstraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
               analyzed = analyzed + char.upper()

        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
    if(removepunc !="on" and fullcaps !="on" and newlineremover !="on" and exstraspaceremover !="on"):
        return  HttpResponse("please select the operation")


    return render(request, 'analyze.html', params)

