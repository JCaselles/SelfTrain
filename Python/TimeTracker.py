#!/usr/bin/env python

#This programm will write to a file the time I spend doing a concret task.
#To acomplish this, I will use the standard text writting and reading tool

#TODO: writting to file code
#TODO: Correct layout
#TODO: Find better way to stop the program until enter click

#import time module for local time reference
import time

#Defining method to get the remaining time
def getTimeReminder (startTime, stopTime, timeRange = 60):
    """
    Function to get the extra time elapsed when it's less than the time hierarchy immediately superior

    :arg startTime: Time of the start of the sequence
    :arg stopTime: Time when the sequence stops
    :arg timeRange: range of the immediately superior time value. Default = 60 (as minutes or seconds)

    :return: The time extra that doesn't fill a whole superior unit
    """
    return (stopTime - startTime)%timeRange


print "\n", "-"*41, "\nGoody, my dear. Start working right away!\n", "-"*41, "\n\n"

#Asking for task name
taskName = raw_input("Enter your task's name: ")


#We use raw_input without variable to ask for enter, and stop the program 
raw_input("\n\nWhen you click enter, we'll start!") # TODO: find a better way to do this

#Now we display the starting conditions
timeSeconds = time.time()#We will store this for the sake of process economy
timeStruct = time.localtime(timeSeconds)#We use the time module to get the local current time
month, day, hour, minute, second =timeStruct[1:6]#We unpack the struct_time into these 5 variables, see documentation of time module for details
weekDay = time.strftime ("%A", timeStruct)#We get the full name of the week with this function
monthName = time.strftime ("%B", timeStruct)

print """

Task name: %s
Starts on: %s, %i of %s
At: %.2i:%.2i:%.2i

""" % (taskName, weekDay, day, monthName, hour, minute, second)

print "-"*41

#print "\n\n Task name: ", taskName, "\nStarts on: ",weekDay.strip(), ", ", str(day).strip(), " of ", monthName.strip(), "\nAt: ", str(hour).strip(), ":", str(minute).strip(), ":", str(second).strip(), "\n\n", "-"*41, "\n\n"

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
                print stopMinute - minute, " minute(s)", getTimeReminder(second, stopSecond), " seconds,"
        else:
            print stopHour - hour, " hour(s)", getTimeReminder (minute, stopMinute), " minute(s)", getTimeReminder(second, stopSecond), " seconds,"
    else:
        print stopDay - day, " day(s)",  getTimeReminder (hour, stopHour,24), " hour(s)",  getTimeReminder (minute, stopMinute), " minute(s)", getTimeReminder (second, stopSecond), " seconds,"
else :
    print stopMonth - month, " month(s)", getTimeReminder (day, stopDay,31), " day(s)",  getTimeReminder (hour, stopHour,24), " hour(s)",  getTimeReminder (minute, stopMinute), " minute(s)", getTimeReminder (second, stopSecond), " seconds," 
#simple modulo calculation. Python rocks :D

print "\n\nCongratulations, your time has been filed. Now have a rest, you deserve it! See you soon!"

