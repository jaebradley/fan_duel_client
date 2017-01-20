

class UrlBuilder:

    base_url = 'https://api.fanduel.com'
    contests_path = '/contests'

    def __init__(self):
        pass

    @staticmethod
    def build_contest_url():
        return '{}{}'.format(UrlBuilder.base_url, UrlBuilder.contests_path)
