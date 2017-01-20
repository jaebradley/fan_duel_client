from unittest import TestCase

from settings import BASIC_AUTHORIZATION_HEADER_VALUE, X_AUTH_TOKEN_HEADER_VALUE

from fan_duel_client import FanDuelClient


class TestFanDuelClient(TestCase):
    def test_get_contests(self):
        client = FanDuelClient(basic_authorization_header_value=BASIC_AUTHORIZATION_HEADER_VALUE,
                               x_auth_token_header_value=X_AUTH_TOKEN_HEADER_VALUE)

        print client.get_contests()
