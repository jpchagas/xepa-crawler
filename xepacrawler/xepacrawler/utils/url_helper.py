from .date_helper import DateHelper


class UrlHelper:
    def __init__(self):
        self.dh = DateHelper()
        #'http://ceasa.rs.gov.br/tabcotacao/02-03-2021/'

    def current_url(self):
        urls = []
        prefix = r'http://ceasa.rs.gov.br/tabcotacao/'
        data = self.dh.get_current_date()
        url = prefix + data.strftime('%d-%m-%Y') + '/'
        url1 = prefix + 'cotacao-' + data.strftime('%d-%m-%Y') + '/'
        urls.append(url)
        urls.append(url1)
        return urls

    def range_urls(self, begin, end):

        urls = []
        prefix = r'http://ceasa.rs.gov.br/tabcotacao/'
        for data in self.dh.get_dates_range(begin, end):
            url = prefix + data.strftime('%d-%m-%Y') + '/'
            url1 = prefix + 'cotacao-' + data.strftime('%d-%m-%Y') + '/'
            urls.append(url)
            urls.append(url1)

        return urls

        #self.dh.get_dates_range(begin, end)