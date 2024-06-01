"""  Steps to create an OTP Verification System using Python  """
# 1. first, we will create a 6 digit random number.
# 2. then we will store this number to a variable.
# 3. then we need to write a program to send the email
# 4. when sending the email, we need to use the OTP as a number.
# 5. finally we need to request 2 user input, first for the user's email and then for the OTP that the user has received.
import os
import math
import random
import smtplib
digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random()*10)]
    msg = OTP + "is your One Time Password"
"""  this link is for singing the google app password.Please follow as the instruction: https://support.google.com/accounts#topic=3382296  """
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login("Your Gmail Account", "Your App Password")
email_id = input("Please enter your Email: ")
s.sendmail('&&&&&&&&&&&', email_id, msg)
a = input("Please enter your OTP >>: ")
if a == OTP:
    print("Yes, you are verified.")
else:
    print("Please check your OTP again")