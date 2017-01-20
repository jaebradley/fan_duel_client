from unittest import TestCase

from fan_duel_client import FanDuelClient


class TestFanDuelClient(TestCase):
    def test_get_contests(self):
        client = FanDuelClient(basic_authorization_header_value='N2U3ODNmMTE4OTIzYzE2NzVjNWZhYWFmZTYwYTc5ZmM6',
                               x_auth_token_header_value='6c4dc2356b276ed2bb5b22cebf370d4dd987b413c2f7d7d6a83486e4b03ce79d')

        print client.get_contests()
