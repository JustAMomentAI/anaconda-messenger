import pyrebase
config = {
  "apiKey": "AIzaSyB8Pcgzvzgn-LLP6Tccvq7MPgxHLiHzW2o",
  "authDomain": "anaconda-messenger.firebaseapp.com",
  "databaseURL": "https://anaconda-messenger.firebaseio.com",
  "serviceAccount": "./serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()



