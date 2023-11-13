# getting system data for teh date and time by using import
import datetime
currentTime = datetime.datetime.now() # storing the current date and time in a variable
print ("Current date and time: ", currentTime.strftime("%m/%d/%Y %H:%M:%S")) # displaying the current date and time
