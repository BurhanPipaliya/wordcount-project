from django.http import HttpResponse
from django.shortcuts import render
import operator

def homePage(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')

def count(request):
    #Get the text from textarea using request.GET[]
    fulltext=request.GET['fulltext']
    #Split the sentences into the word it will create a list of words
    wordlist = fulltext.split()

    #Get the most repeated words in the word list
    wordcount={}

    for word in wordlist:
        if word in wordcount:
            #increase
            wordcount[word]+=1
        else:
            wordcount[word] = 1

    sortedword=sorted(wordcount.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedword':sortedword})