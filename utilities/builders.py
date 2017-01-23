

class UrlBuilder:

    base_url = 'https://api.fanduel.com'
    contests_path = '/contests'
    fixture_lists_path = '/fixture-lists'

    def __init__(self):
        pass

    @staticmethod
    def build_contest_url():
        return '{}{}'.format(UrlBuilder.base_url, UrlBuilder.contests_path)

    @staticmethod
    def build_fixture_lists_url():
        return '{}{}'.format(UrlBuilder.base_url, UrlBuilder.fixture_lists_path)

    @staticmethod
    def build_fixture_list_players_url(fixture_list_id):
        return '{}/{}/players'.format(UrlBuilder.build_fixture_lists_url(), fixture_list_id)


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
