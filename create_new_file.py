print('-------------------')
print('--CREATE NEW FILE--')
print('-------------------\n\n')
fName = input('What do you want to file to be named? ')
fType = input('What is the file type? (md or txt) ')

if fType == 'md':
    print('----------------------------')
    print('--CREATE NEW MARKDOWN FILE--')
    print('----------------------------\n\n')
    fileBody = input('What do you want inside the file? ')
    file = open(fName+'.md', 'w')
    file.write(fileBody)
    file.close()

elif fType == 'txt':
    print('------------------------')
    print('--CREATE NEW TEXT FILE--')
    print('------------------------\n\n')
    fileBody = input('What do you want inside the file? ')
    file = open(fName+'.txt', 'w')
    file.write(fileBody)
    file.close()

else:
    print('Sorry could not understand file type')
