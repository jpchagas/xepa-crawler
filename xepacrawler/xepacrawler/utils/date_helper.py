from datetime import datetime, timedelta, date

class DateHelper:
    def __init__(self):
        pass

    def get_current_date(self):
        return date.today()

    def get_dates_range(self, begin, end):
        date_rage = []
        bstring = datetime.strptime(begin, '%d/%m/%y %H:%M:%S')
        estring = datetime.strptime(end, '%d/%m/%y %H:%M:%S')
        sdate = date(bstring.year, bstring.month, bstring.day)  # start date
        edate = date(estring.year, estring.month, estring.day)  # end date

        delta = edate - sdate  # as timedelta

        for i in range(delta.days + 1):
            day = sdate + timedelta(days=i)
            date_rage.append(day)

        return date_rage