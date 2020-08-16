import requests
from firebase import firebase
print('-------------------')
print('--CREATE NEW IDEA--')
print('-------------------\n')


def main_choice():
    result = input("Add new idea? or Skip to overview? (Add/Skip)")
    return result


def overview(inputText):
    if inputText == 'N':
        print('Not printing overview...')

        print('\n-------------------')
        print('--CREATE NEW IDEA--')
        print('-------------------')
    elif inputText == 'Y':
        print('\n--------------------------')
        print('-- printing overview... --')
        print('--------------------------')
        # print(ideasList)
        print(ideas)
    else:
        print('Sorry I didn\'t understand that, please try again.')


if __name__ == '__main__':

    firebase = firebase.FirebaseApplication(
        'https://personal-testing-445c1.firebaseio.com/', None)
    get_ideas_list = firebase.get('/ideas', None)

    ideas = []
    for i in get_ideas_list:
        # ideasList.append(i)
        newIdea = firebase.get('/ideas/' + i, None, {'print': 'pretty'})
        ideas.append(newIdea)

    if main_choice() == 'Skip':

        overviewInput = input('\n\nDo you want to see an overview? (Y/N)')
        print(overviewInput)

        overview(overviewInput)

    elif main_choice() == 'Add':
        new_idea_title = input('What\'s your Idea Title? ')
        new_idea_body = input('What\'s your Idea? ')
        new_idea = {
            'title': new_idea_title,
            'body': new_idea_body,
        }
        post_new_idea = firebase.post('/ideas', new_idea)
        print('\n'+str(post_new_idea))
        print(new_idea)

        overviewInput = input('\n\nDo you want to see an overview? (Y/N)')
        print(overviewInput)

        overview(overviewInput)

    else:

        print('\n-------------------')
        print('--CREATE NEW IDEA--')
        print('-------------------')
