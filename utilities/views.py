from django.shortcuts import render
import custom
# Create your views here.
def loginPage(request):
    return render(request, "index.html" )
def homePage(request):
    return render(request, "home.html" )
#def updateMessages(request):
def goToSetMeetingsAndIdeas(request):
    return render(request, "generate.html")
def setMeeting(request):
    custom.resolveMeetingData(request)
    return render(request, "generate.html")
