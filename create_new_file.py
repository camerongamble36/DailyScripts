print('-------------------')
print('--CREATE NEW FILE--')
print('-------------------\n\n')
fName = input('What do you want to file to be named? ')
fType = input('What is the file type? (md, txt, or other) ')

if fType != "txt" or "md":
    print('--------------------------')
    print('--CREATE NEW CUSTOM FILE--')
    print('--------------------------\n\n')
    fileBody = input('What do you want inside the file? ')
    if fType[0] == ".":
        file = open(fName + fType, 'w')
        file.write(fileBody)
        file.close()
    else:
        file = open(fName + "." + fType, 'w')
        file.write(fileBody)
        file.close()

elif fType == 'md' or "markdown":
    print('----------------------------')
    print('--CREATE NEW MARKDOWN FILE--')
    print('----------------------------\n\n')
    fileBody = input('What do you want inside the file? ')
    file = open(fName+"."+fType, 'w')
    file.write(fileBody)
    file.close()

elif fType == 'txt' or "text":
    print('------------------------')
    print('--CREATE NEW TEXT FILE--')
    print('------------------------\n\n')
    fileBody = input('What do you want inside the file? ')
    file = open(fName+"."+fType, 'w')
    file.write(fileBody)
    file.close()

else:
    print('Sorry could not understand file type')
