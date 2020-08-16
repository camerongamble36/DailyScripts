from firebase import firebase
print('-------------------')
print('--CREATE NEW IDEA--')
print('-------------------\n\n')

firebase = firebase.FirebaseApplication(
    'https://personal-testing-445c1.firebaseio.com/', None)

new_idea = input('What\'s your idea? ')
result = firebase.post('/ideas', new_idea)

print(result)
