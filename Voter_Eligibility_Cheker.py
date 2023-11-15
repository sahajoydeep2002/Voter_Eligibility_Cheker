import datetime
from datetime import timedelta
now = datetime.datetime.now()
vote_date_time = '24th March 2024 between 10 AM to 4PM'
vote_date = 'March 24, 2023'
vote_date_time_st = datetime.datetime.strptime(vote_date, '%B %d, %Y')
delta = (now-vote_date_time_st)
years = delta.days // 365
months = (delta.days % 365) // 30
days = (delta.days % 365) % 30
year_text = "just" if years == 0 else f"{years} Years"
month = "and" if months == 0 else f"{months} Year"

def voter_age(check_age):
    if (now - birth_date) >= timedelta(days= 18*365):
        return f"Horrah! You are eligible to vote, and you can attend the next vote on {vote_date_time} which is {year_text} Year {months} months, and {days} days away, please wait patiently!"
    else:
        age_delta = (birth_date + timedelta(days= 18 * 365)) - now
        years_left = (age_delta.days) // 365
        months_left = (age_delta.days % 365) // 30
        days_left = (age_delta.days % 365) % 30
        year_alpha = "just" if years_left == 0 else f"{years_left} Years"
        month_alpha = " " if years_left== 0 else f"{months_left} Months and,"
        return f"Ohho! I saw that you wished to vote, but you are not 18 Yet to vote, you have to wait {year_alpha}{month_alpha} {days_left} Days after which you'll be eliglble to vote"

user = input('Do you wish to know your voting status? (Yes/No) ')

while True:

  if user in ('Yes', 'yes', 'YES'):

    birth_date_str = input('What is your date of birth in DD/MM/YYYY format? (e.g., 01/01/2000): ')

    try:
        birth_date = datetime.datetime.strptime(birth_date_str, '%d/%m/%Y')
        print(voter_age(birth_date))

    except ValueError:
        print("Invalid date format. Please use the DD/MM/YYYY format, e.g., 01/01/2000.")

  elif user in ('No', 'no', 'NO'):
     print ('not an issue, sayonara')
     break

  else:
    print('Invalid input. Please enter Yes or No.')
    user = input('Do you wish to know your voting status? (Yes/No) ')
