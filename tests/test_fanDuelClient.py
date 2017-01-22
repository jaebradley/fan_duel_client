from unittest import TestCase

from settings import BASIC_AUTHORIZATION_HEADER_VALUE, X_AUTH_TOKEN_HEADER_VALUE

from fan_duel_client import FanDuelClient


class TestFanDuelClient(TestCase):
    client = FanDuelClient(basic_authorization_header_value=BASIC_AUTHORIZATION_HEADER_VALUE,
                           x_auth_token_header_value=X_AUTH_TOKEN_HEADER_VALUE)

    def test_get_contests(self):
        for contest in self.client.get_contests():
            print contest.__dict__

    def test_get_fixtures(self):
        for fixture in self.client.get_fixtures():
            print fixture.__dict__


