import datetime
print("-----------------------------------------------------")
print("------------------- Day Overview --------------------")
print('-----------------------------------------------------\n\n')
now = datetime.datetime.now()
openToTasks = True
print("The current Date is: " + str(now.year) +
      "-" + str(now.month) + "-" + str(now.day))

if (now.hour == 13):
    print("The current Time is: " + str(1) +
          ":" + str(now.minute) + " PM")
elif (now.hour == 14):
    print("The current Time is: " + str(2) +
          ":" + str(now.minute) + " PM")
elif (now.hour == 15):
    print("The current Time is: " + str(3) +
          ":" + str(now.minute)+" PM")
elif (now.hour == 16):
    print("The current Time is: " + str(4) +
          ":" + str(now.minute)+" PM")
elif (now.hour == 17):
    print("The current Time is: " + str(5) +
          ":"+str(now.minute)+" PM")
elif (now.hour == 18):
    print("The current Time is: " + str(6) +
          ":" + str(now.minute) + " PM")
elif (now.hour == 19):
    print("The current Time is: " + str(7) +
          ":"+str(now.minute)+" PM")
elif (now.hour == 20):
    print("The current Time is: " + str(8) +
          ":" + str(now.minute) + " PM")
elif (now.hour == 21):
    print("The current Time is: " + str(9) +
          ":"+str(now.minute)+" PM")
elif (now.hour == 16):
    print("The current Time is: " + str(10) +
          ":" + str(now.minute) + " PM")
elif (now.hour == 16):
    print("The current Time is: " + str(11) +
          ":" + str(now.minute) + " PM")
elif (now.hour == 16):
    print("The current Time is: " + str(12) +
          ":"+str(now.minute)+" PM")
else:
    print("The current Time is: " + str(now.hour) +
          ":"+str(now.minute)+" PM")

tasksList = []
task_descision = input(
    '\nDo you have any tasks you want to do today? (Y or N) ')

if task_descision == 'Y':

    new_task = input('What should your new task be? ')
    tasksList.append(new_task)
    print("\n"+new_task + " has been added to tasks for today")
    print('Tasks List:\n' + str(tasksList))

elif task_descision == 'N':
    print('No new tasks today')

else:
    print('Sorry I don\'t understand, can you try again')

print("\n\n-----------------------------------------------------")
print("------------------- Day Overview --------------------")
print('-----------------------------------------------------')
