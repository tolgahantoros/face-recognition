import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://deneme1-338d2-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "105461": {
      "last_attendance_time": "2022-12-11 00:54:34",
      "major": "Dr. Ogr. G.",
      "name": "Mehmat Acı",
      "standing": "G",
      "starting_year": 2023,
      "total_attendance": 0,
      "year": 1
    },
    "131313": {
      "last_attendance_time": "2022-12-11 00:54:34",
      "major": "Prof",
      "name": "Zeki Yetgin",
      "standing": "G",
      "starting_year": 2023,
      "total_attendance": 0,
      "year": 1
    },
    "321654": {
      "last_attendance_time": "2023-10-27 21:49:47",
      "major": "Ogrenci",
      "name": "Tolgahan Toros",
      "standing": "G",
      "starting_year": 2023,
      "total_attendance": 0,
      "year": 1
    },
    "852741": {
      "last_attendance_time": "2023-07-11 14:00:00",
      "major": "Ogrenci",
      "name": "Sabri Kucuk",
      "standing": "B",
      "starting_year": 2023,
      "total_attendance": 0,
      "year": 1
    },
    "963852": {
      "last_attendance_time": "2023-10-12 12:47:25",
      "major": "Ogrenci",
      "name": "Emin Hezer",
      "standing": "G",
      "starting_year": 2023,
      "total_attendance": 0,
      "year": 1
    }

}

for key, value in data.items():
    ref.child(key).set(value)