from django import forms

class MeetingForm(forms.Form):
    date = forms.DateField(input_formats= ('%Y-%m-%d',))
    time = forms.TimeField(input_formats= ('%H:%M',))
    content = forms.CharField(max_length = 1000)
    note = forms.CharField(max_length = 2000)