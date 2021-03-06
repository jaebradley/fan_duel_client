from unittest import TestCase

from settings import BASIC_AUTHORIZATION_HEADER_VALUE, X_AUTH_TOKEN_HEADER_VALUE

from fan_duel_client import FanDuelClient


class TestFanDuelClient(TestCase):
    client = FanDuelClient(basic_authorization_header_value=BASIC_AUTHORIZATION_HEADER_VALUE,
                           x_auth_token_header_value=X_AUTH_TOKEN_HEADER_VALUE)

    def test_get_contests(self):
        for contest in self.client.get_contests():
            print contest.__dict__

    def test_get_fixture_lists(self):
        for fixture in self.client.get_fixture_lists():
            print fixture.__dict__

    def test_get_fixture_players(self):
        fixture_list_id = 17722
        for fixture_player in self.client.get_fixture_players(fixture_list_id=fixture_list_id):
            print fixture_player.__dict__
