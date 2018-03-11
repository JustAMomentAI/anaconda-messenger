import pyrebase
from django.db import models

config = {
  "apiKey": "AIzaSyB8Pcgzvzgn-LLP6Tccvq7MPgxHLiHzW2o",
  "authDomain": "anaconda-messenger.firebaseapp.com",
  "databaseURL": "https://anaconda-messenger.firebaseio.com",
  "storageBucket": "anaconda-messenger.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

class Meeting(models.Model):
  date = models.DateField();
  time = models.TimeField();
  content =  models.CharField(max_length = 1000);
  note = models.CharField(max_length = 2000);



