from datetime import datetime
from enum import Enum

# TODO: @jbradley not all sports are represented - add sports as they are identified


class Sport(Enum):
    nba = 'nba'
    nhl = 'nhl'
    nfl = 'nfl'

    @staticmethod
    def value_of(name):
        assert isinstance(name, basestring)

        for sport in Sport:
            if sport.value == name.lower():
                return sport

        raise ValueError('Unknown sport: %s', name)

# TODO: @jbradley not all fields in Contest JSON are represented - add fields as needed


class Contest:
    def __init__(self, contest_id, max_entries_per_user, name, is_guaranteed, url, entry_fee):
        assert isinstance(contest_id, basestring)
        assert isinstance(max_entries_per_user, int)
        assert isinstance(name, basestring)
        assert isinstance(is_guaranteed, bool)
        assert isinstance(url, basestring)
        assert isinstance(entry_fee, int)

        self.contest_id = contest_id
        self.max_entries_per_user = max_entries_per_user
        self.name = name
        self.is_guaranteed = is_guaranteed
        self.url = url
        self.entry_fee = entry_fee


class FixtureStatus:
    def __init__(self, has_started, is_final):
        assert isinstance(has_started, bool)
        assert isinstance(is_final, bool)

        self.has_started = has_started
        self.is_final = is_final


class Fixture:
    def __init__(self, fixture_id, url, status, start_time, players_url, sport, salary_cap):
        assert isinstance(fixture_id, basestring)
        assert isinstance(url, basestring)
        assert isinstance(status, FixtureStatus)
        assert isinstance(start_time, datetime)
        assert isinstance(players_url, basestring)
        assert isinstance(sport, Sport)
        assert isinstance(salary_cap, int)

        self.fixture_id = fixture_id
        self.url = url,
        self.start_time = start_time
        self.players_url = players_url
        self.sport = sport
        self.salary_cap = salary_cap
