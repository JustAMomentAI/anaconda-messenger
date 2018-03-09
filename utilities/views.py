from django.shortcuts import render

# Create your views here.
def loginPage(request):
    return render(request, "index.html" )
def homePage(request):
    return render(request, "home.html" )
#def updateMessages(request):
