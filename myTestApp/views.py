from django.shortcuts import render
from django.http import HttpResponse
from myTestApp.models import MyBookModel

"""def index(request):
    return HttpResponse("Hello world!")"""

def index(request):
    # uses the defined templates section to find the templates so it's not much of a problem for it.
    books = MyBookModel.objects.all().values()
    output = "the books:\n"
    output_long = "the long books:\n "
    for book in books:
        output += book['title']
        output_long += str(book)
    return render(request,"test.html",{'output':output,'output_long':output_long})
