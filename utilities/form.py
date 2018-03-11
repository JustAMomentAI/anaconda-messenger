from django import forms

class MeetingForm(forms.Form):
    date = forms.DateField(input_formats= ('%m/%d/%Y',))
    time = forms.TimeField(input_formats= ('%I:%M %p',))
    content = forms.CharField(max_length = 1000)
    note = forms.CharField(max_length = 2000)