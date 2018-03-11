from django import forms

class MeetingForm(forms.Form):
    date = forms.DateField(input_formats= ('%d/%m/%Y',), widget = forms.DateInput(attrs={"class":'w3-input w3-padding-16'}))
    time = forms.TimeField(input_formats= ('%H:%M',),widget = forms.TimeInput(attrs={"class" : 'w3-input w3-padding-16'}))
    content = forms.CharField(max_length = 1000, widget = forms.TextInput(attrs={"class": 'w3-input w3-padding-16'}))
    note = forms.CharField(max_length = 2000, widget = forms.TextInput(attrs={"class": 'w3-input w3-padding-16'}))