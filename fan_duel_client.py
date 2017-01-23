import requests

from data.deserializers import ContestsDeserializer, FixtureListsDeserializer
from utilities.builders import UrlBuilder, HeadersBuilder


class FanDuelClient:
    def __init__(self, basic_authorization_header_value, x_auth_token_header_value):
        self.headers = HeadersBuilder.build(basic_authorization_header_value=basic_authorization_header_value,
                                            x_auth_token_header_value=x_auth_token_header_value)

    def get_contests(self):
        response = requests.get(url=UrlBuilder.build_contest_url(), headers=self.headers)

        response.raise_for_status()

        return ContestsDeserializer.deserialize(contests_json=response.json())

    def get_fixtures(self):
        response = requests.get(url=UrlBuilder.build_fixtures_url(), headers=self.headers)

        response.raise_for_status()

        return FixtureListsDeserializer.deserialize(fixture_lists_json=response.json())
