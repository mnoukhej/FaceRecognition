import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendence-6b62b-default-rtdb.firebaseio.com/"
})

ref = db.reference('students')

data = {
    '1592648':
    {
        'name': 'Muhammad Noukhez',
        'major': 'Robotics',
        'starting_year': 2022,
        'total_attendance': 6,
        'standing': 'G',
        'year': 2,
        'last_attendance_time': '2023-11-10 00:54:34'
    },

    '1592649':
    {
        'name': 'Yousuf Ansari',
        'major': 'Machine Learning',
        'starting_year': 2019,
        'total_attendance': 14,
        'standing': 'G',
        'year': 5,
        'last_attendance_time': '2023-11-08 00:30:34'
    },

    '1592650':
    {
        'name': 'Mustafizur Rahaman',
        'major': 'Robotics',
        'starting_year': 2021,
        'total_attendance': 10,
        'standing': 'G',
        'year': 4,
        'last_attendance_time': '2023-11-09 00:24:34'
    }
}

for key, value in data.items():
    ref.child(key).set(value)