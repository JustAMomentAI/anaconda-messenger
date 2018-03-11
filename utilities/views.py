from django.shortcuts import render
from . import custom
from .form import MeetingForm, IdeaForm

# Create your views here.
def loginPage(request):
    return render(request, "index.html" )
def homePage(request):
    usersList = custom.getUserChatmates()
    return render(request, "home.html", {'usersList' : usersList})
#def updateMessages(request):
def goToSetMeetingsAndIdeas(request):
    return render(request, "generate.html", {'form': MeetingForm(), 'ideaForm' : IdeaForm()})
def setMeeting(request):
    if(request.method == "POST"):
        print("first step")
        meetingForm = MeetingForm(request.POST)
        if meetingForm.is_valid():
            data = {
                'date' : meetingForm.cleaned_data['date'],
                'time' : meetingForm.cleaned_data['time'],
                'content' : meetingForm.cleaned_data['content'],
                'note' : meetingForm.cleaned_data['note']
            }
            custom.resolveMeetingData(data)
        else:

            return render(request, "generate.html", {'error' : 'wrong format. Please note the instructions', 'form' : MeetingForm()})
    else:
        meetingForm = MeetingForm()
    return render(request, "generate.html", {'form' : meetingForm, "ideaForm" : IdeaForm()})

def setIdeas(request):
    if(request.method == "POST"):
        print("first step")
        ideaForm = IdeaForm(request.POST)
        if ideaForm.is_valid():
            data = {
                'content' : ideaForm.cleaned_data['type'],
            }
            custom.resolveIdeaData(data)
        else:
            return render(request, "generate.html", {'error' : 'wrong format. Please note the instructions',  : })
    else:
        ideaForm = IdeaForm()
    return render(request, "generate.html", {'form' : MeetingForm(), "ideaForm" : ideaForm})