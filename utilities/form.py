from django import forms

class MeetingForm(forms.Form):
    date = forms.DateField(input_formats= ('%m/%d/%Y',), widget = forms.DateInput(attrs={"class":'w3-input w3-padding-16','placeholder' :'mm/dd/yy'}))
    time = forms.TimeField(input_formats= ('%H:%M',),widget = forms.TimeInput(attrs={"class" : 'w3-input w3-padding-16','placeholder' :'hh:mm. Ex: 13:00 , 09:28'}))
    content = forms.CharField(max_length = 1000, widget = forms.TextInput(attrs={"class": 'w3-input w3-padding-16','placeholder' :'content of the meeting'}))
    note = forms.CharField(max_length = 2000, widget = forms.TextInput(attrs={"class": 'w3-input w3-padding-16', 'placeholder' :'some note'}))

class IdeaForm(forms.Form):
    description = forms.CharField(max_length= 1000, widget = forms.Textarea(attrs= {'class' : 'w3-input w3-padding-16', 'placeholder' :'no more 100 words'}))