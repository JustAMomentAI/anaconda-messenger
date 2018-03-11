from django import forms
from .models import Meeting
class MeetingForm(forms.Form):
    model = Meeting
    field = ("date", "time","content", "note")