from .date_helper import DateHelper


class UrlHelper:
    def __init__(self):
        self.dh = DateHelper()
        #'http://ceasa.rs.gov.br/tabcotacao/02-03-2021/'

    def current_url(self):
        urls = []
        prefix = r'http://ceasa.rs.gov.br/tabcotacao/' + self.dh.get_current_date() + '/'
        urls.append(prefix)
        return urls

    def range_urls(self, begin, end):
        urls = []
        prefix = r'http://ceasa.rs.gov.br/tabcotacao/'
        for data in get_dates():
            if data > date(2020, 1, 8):
                url = prefix + data.strftime('%d-%m-%Y') + '/'
            elif data == date(2020, 1, 8):
                url = prefix + '2339' + '/'
            else:
                url = prefix + 'cotacao-' + data.strftime('%d-%m-%Y') + '/'
            urls.append(url)

        return urls