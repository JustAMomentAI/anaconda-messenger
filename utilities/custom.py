import json
from django.dispatch import receiver
from allauth.account import signals
from . import models
def resolveMeetingData(data):
    models.db.child("meetings").push(data)
def resolveIdeaData(data):
    models.db.child("ideas").push(data)
def getUserChatmates():
    return models.db.child("users").get().val()       

@receiver (signals.user_logged_in)
def savingUserData(sender, **kwargs):
    user = kwargs.pop('user')
    #save user data
    userData = {
        'profile_pic' : user.socialaccount_set.filter(provider = 'facebook')[0].get_avatar_url(),
        'name' : user.socialaccount_set.filter(provider = 'facebook')[0].extra_data['name']
    }    
    uid = user.socialaccount_set.filter(provider = 'facebook')[0].extra_data['id']
    
    models.db.child('users/'+uid).set(userData)



    