from datetime import datetime, timedelta, date

class DateHelper:
    def __init__(self):
        pass

    def get_current_date(self):
        return date.today()

    def get_dates_range(self):
        sdate = date(2008, 8, 15)  # start date
        edate = date(2008, 9, 15)  # end date

        delta = edate - sdate  # as timedelta

        for i in range(delta.days + 1):
            day = sdate + timedelta(days=i)
            print(day)