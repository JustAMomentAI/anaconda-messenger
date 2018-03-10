import json
from django.dispatch import receiver
from allauth.account import signals
from . import models
def resolveMeetingData(request):
    if(request.method == "POST"):
        #GIVE ME STH
        meetingData = json.loads(request.body.decode('utf-8'))
        models.db.child("meetings").set(meetingData)
        #save meetingData

@receiver (signals.user_logged_in)
def savingUserData(sender, **kwargs):
    user = kwargs.pop('user')
    #save user data
    userData = {
        'profile_pic' : user.socialaccount_set.filter(provider = 'facebook')[0].get_avatar_url(),
        'name' : user.socialaccount_set.filter(provider = 'facebook')[0].extra_data['name'],
        'uid' : user.socialaccount_set.filter(provider = 'facebook')[0].extra_data['id']
    }
    models.db.child('users').set(userData)



    