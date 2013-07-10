#!/usr/bin/env python

#This programm will write to a file the time I spend doing a concret task.
#To acomplish this, I will use the standard text writting and reading tool

#TODO: writting to file code

#import time module for local time reference
import time

print "\n", "-"*41, "\nGoody, my dear. Start working right away!\n", "-"*41, "\n\n"

#Asking for task name
taskName = raw_input("Enter your task's name: ")


#We use raw_input without variable to ask for enter, and stop the program 
raw_input("\n\nWhen you click enter, we'll start!") # TODO: find a better way to do this

#Now we display the starting conditions
timeSeconds = time.time()#We will store this for the sake of process economy
timeStruct = time.localtime(timeSeconds)#We use the time module to get the local current time
month, day, hour, minute, second = timeStruct[1:6]#We unpack the struct_time into these 5 variables, see documentation of time module for details
weekDay = time.strftime ("%A", timeStruct)#We get the full name of the week with this function
monthName = time.strftime ("%B", timeStruct)

print "\n\n Task name: ", taskName, "\nStarts on: ",weekDay, ", ", day, " of ", monthName, "\nAt: ", hour, ":", minute, ":", second, "\n\n", "-"*41, "\n\n"
raw_input ("Click enter to stop the clock.")

#When user stops the clock, we register the time and write it in a file
stopTimeSeconds = time.time()
stopTimeStruct = time.localtime(stopTimeSeconds)
stopMonth, stopDay, stopHour, stopMinute, stopSecond = stopTimeStruct[1:6]

print "You've spent ",
if stopMonth == month:
    if stopDay == day:
        if stopHour == hour:
            if stopMinute == minute:
                if stopSecond != second:
                    print stopSecond - second, " seconds."
            else:
                print stopMinute - minute, " minute(s)", stopSecond - second, " seconds,"
        else:
            print stopHour - hour, " hour(s)",  stopMinute - minute, " minute(s)", stopSecond - second, " seconds,"
    else:
        printstopDay - day, " day(s)",  stopHour - hour, " hour(s)",  stopMinute - minute, " minute(s)", stopSecond - second, " seconds,"
else :
    print stopMonth - month, " month(s)", stopDay - day, " day(s)",  stopHour - hour, " hour(s)",  stopMinute - minute, " minute(s)", stopSecond - second, " seconds," 
# FIXME: What to do when time is negative, without too many if's?

print "\n\nCongratulations, your time has been filed. Now have a rest, you deserve it! See you soon!"

