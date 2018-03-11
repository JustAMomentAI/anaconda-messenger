from django.shortcuts import render
from . import custom, form
# Create your views here.
def loginPage(request):
    return render(request, "index.html" )
def homePage(request):
    usersList = custom.getUserChatmates()
    return render(request, "home.html", usersList)
#def updateMessages(request):
def goToSetMeetingsAndIdeas(request):
    return render(request, "generate.html")
def setMeeting(request):
    if(request.method == "POST"):
        meetingForm = form.MeetingForm(request.POST);
        if meetingForm.is_valid():
            print (meetingForm.cleaned_data["date"])
        else:
            print("fuck");
    return render(request, "generate.html")
