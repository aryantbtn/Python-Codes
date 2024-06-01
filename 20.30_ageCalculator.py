# Age Calculaator is an amazing application to create as a beginner in any programiing language. To craete an age calculator, you need two dates:

"""
today date
date of birth(D.O.B) """
def age_calculator(year, month, date):
    import datetime
    today = datetime.datetime.now().date()
    date_of_birth = datetime.date(year,month,date)
    age = (today - date_of_birth).days/365.25
    print(int(age))
age_calculator(1941, 11, 9)