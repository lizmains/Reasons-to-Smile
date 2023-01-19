from flask import Flask, render_template, redirect, url_for, request
import fileinput
import random
import calendar
from datetime import date
import smtplib
import datetime
import platform
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# import system

# prints out system info
# print(sys.executable)

# print python version
print("PYTHON VERSION")
print(platform.python_version())
print("PYTHON VERSION")

# picking a random number from a list
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
x = random.choice(numList)
print("random number selector: ")
print(random.choice(numList))

# prints todays date
today = date.today()  # numbers
curr_date = date.today()  # words
print("Today's date: ")
print("Today is: ", calendar.day_name[curr_date.weekday()], today)

# line counter
doc = open("infoFiles/reasonsToSmile", "r")  # Reasons to smile
cont = doc.readlines()  # read lines
line_count = 0  # set up int
for line in doc:
    if line != "\n":
        line_count += 1  # run through doc
# doc.close()
print("Line count for reasons to smile: ")
print(line_count)

doc2 = open("infoFiles/nationalHolidays", "r")  # National holidays
cont2 = doc2.readlines()
line_count2 = 0
for line2 in doc2:
    if line2 != "\n":
        line_count2 += 1
# doc2.close()
print("Line count for national holidays: ")
print(line_count2)

currentDay = datetime.datetime.now()
print("Current day: ")
print(currentDay.day)
print("day - 1: ")
print(cont[int(currentDay.day - 1)])
print("Current day again: ")
print(currentDay.day)

dayOfYear = currentDay.timetuple().tm_yday  # get number of the day
todayIs = str(calendar.day_name[curr_date.weekday()]) + " " + str(today)  # gets date
rtm = str(cont[dayOfYear - 1]).strip()  # pulls reason to smile from list
natHol = str(cont2[dayOfYear - 1]).strip()  # pulls national holiday

# create and print todays message
print(dayOfYear)

todMessage = "Hello! \nToday is " + todayIs + " and it is " \
             + natHol + "!" \
             + "\nTodays reason to smile is " + rtm \
             + "\nMake today a great one :)"
print(todMessage)

# open and connect to email
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("TodaysReasonsToSmile", "Reasons2Smile")

# #SEND TO EVERYONEa
# send email to everyone on text file
email = open("infoFiles/emails")
numLines = 19
for i in range(numLines):
    lines = email.readline()
    msg = MIMEMultipart()
    msg['From'] = "RTS"
    msg['To'] = lines
    msg['Subject'] = "Reason to Smile"

    # add in the message body
    msg.attach(MIMEText(todMessage, 'plain'))
    s.send_message(msg)

# #SEND TO JUST ME
# msg = MIMEMultipart()
# msg['From'] = "RTS"
# msg['To'] = "emains@ycp.edu"
# msg['Subject'] = "Reason to Smile"
#
# # add in the message body
# msg.attach(MIMEText(todMessage, 'plain'))
# s.send_message(msg)
# s.quit()


app = Flask(__name__)


@app.route('/')
def welcome():  # put application's code here
    return render_template('welcome.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    return render_template('logout.html')


@app.route('/rtsEntry')
def rtsEntry():
    return render_template('rtsEntry.html')


@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')


@app.route('/unsubscribe')
def unsubscribe():
    return render_template('unsubscribe.html')


if __name__ == '__main__':
    app.run()
