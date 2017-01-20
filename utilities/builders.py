

class UrlBuilder:

    base_url = 'https://api.fanduel.com'
    contests_path = '/contests'

    def __init__(self):
        pass

    @staticmethod
    def build_contest_url():
        return '{}{}'.format(UrlBuilder.base_url, UrlBuilder.contests_path)


class HeadersBuilder:

    host_value = 'api.fanduel.com'
    origin_value = 'https://www.fanduel.com'
    referer_value = 'https://www.fanduel.com/games'

    def __init__(self):
        pass

    @staticmethod
    def build(basic_authorization_header_value, x_auth_token_header_value):
        return {
            'Authorization': 'Basic {}'.format(basic_authorization_header_value),
            'X-Auth-Token': x_auth_token_header_value,
            'Host': HeadersBuilder.host_value,
            'Origin': HeadersBuilder.origin_value,
            'Referer': HeadersBuilder.referer_value
        }
