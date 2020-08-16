from firebase import firebase
print('-------------------')
print('--CREATE NEW WW--')
print('-------------------\n\n')

firebase = firebase.FirebaseApplication(
    'https://personal-testing-445c1.firebaseio.com/', None)

print("Create New Weird Workout")
workout_title = input('Title: ')
workout_desc = input('Description: ')
workout_sets = input('Sets: ')
workout_reps = input('Reps: ')

new_workout = {
    'title': workout_title,
    'description': workout_desc,
    'sets': workout_sets,
    'reps': workout_reps
}
result = firebase.post('/weird-workouts', new_workout)
print(result)

print('-------------------')
print('--WEIRD WORKOUTS--')
print('-------------------\n\n')
