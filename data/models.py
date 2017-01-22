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


class FixtureListStatus:
    def __init__(self, has_started, is_final):
        assert isinstance(has_started, bool)
        assert isinstance(is_final, bool)

        self.has_started = has_started
        self.is_final = is_final


class FixtureList:
    def __init__(self, fixture_id, url, status, start_time, players_url, sport, salary_cap):
        assert isinstance(fixture_id, basestring)
        assert isinstance(url, basestring)
        assert isinstance(status, FixtureListStatus)
        assert isinstance(start_time, datetime)
        assert isinstance(players_url, basestring)
        assert isinstance(sport, Sport)
        assert isinstance(salary_cap, int)

        self.fixture_list_id = fixture_id
        self.url = url,
        self.status = status
        self.start_time = start_time
        self.players_url = players_url
        self.sport = sport
        self.salary_cap = salary_cap


class Team(Enum):
    atlanta_hawks = 679
    boston_celtics = None
    brooklyn_nets = 696
    charlotte_hornets = 681
    chicago_bulls = 682
    cleveland_cavaliers = None
    dallas_mavericks = 684
    denver_nuggets = 685
    detroit_pistons = None
    golden_state_warriors = 687
    houston_rockets = 688
    indiana_pacers = 689
    los_angeles_clippers = None
    los_angeles_lakers = 691
    memphis_grizzlies = 692
    miami_heat = None
    milwaukee_bucks = 694
    minnesota_timberwolves = 695
    new_orleans_pelicans = 697
    new_york_knicks = None
    oklahoma_city_thunder = None
    orlando_magic = 700
    philadelphia_76ers = 701
    phoenix_suns = 702
    portland_trail_blazers = 703
    sacramento_kings = 704
    san_antonio_spurs = None
    toronto_raptors = 706
    utah_jazz = 707
    washington_wizards = None


class Position(Enum):
    point_guard = {
        'sport': Sport.nba,
        'abbreviation': 'PG'
    }
    shooting_guard = {
        'sport': Sport.nba,
        'abbreviation': 'SG'
    }
    small_forward = {
        'sport': Sport.nba,
        'abbreviation': 'SF'
    }
    power_forward = {
        'sport': Sport.nba,
        'abbreviation': 'PF'
    },
    center = {
        'sport': Sport.nba,
        'abbreviation': 'C'
    }


class FixtureStatus:
    def __init__(self, is_final, has_started):
        self.is_final = is_final
        self.has_started = has_started


class Fixture:
    def __init__(self, fixture_id, sport, status, away_team, home_team, start_time):
        self.fixture_id = fixture_id
        self.sport = sport
        self.status = status
        self.away_team = away_team
        self.home_team = home_team
        self.status = status
        self.start_time = start_time


class FixturePlayerInjury:
    def __init__(self, details, status):
        assert isinstance(details, basestring)
        assert isinstance(status, basestring)

        self.details = details
        self.status = status


class FixturePlayer:
    def __init__(self, fixture_player_id, first_name, last_name, jersey, is_removed, position, salary, team, fixture):
        assert isinstance(fixture_player_id, basestring)
        assert isinstance(first_name, basestring)
        assert isinstance(last_name, basestring)
        assert isinstance(jersey, int)
        assert isinstance(is_removed, bool)
        assert isinstance(position, Position)
        assert isinstance(salary, int)
        assert isinstance(team, Team)
        # assert isinstance(fixture, Fixture)

        self.fixture_player_id = fixture_player_id,
        self.first_name = first_name
        self.last_name = last_name
        self.jersey = jersey
        self.injury = self.injury
        self.is_removed = is_removed,
        self.position = position
        self.salary = salary
        self.team = team
        self.fixture = fixture
