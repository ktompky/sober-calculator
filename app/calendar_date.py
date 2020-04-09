import datetime

def sober_date():
    date_entry = input('Enter a date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)

    today = datetime.date.today()
    diff = (today - date1).days
    return "You have stayed sober for {} days! Good job!!!".format(diff)


sober_date()