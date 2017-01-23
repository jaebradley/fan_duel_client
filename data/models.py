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
    atlanta_hawks = {
        'sport': Sport.nba,
        'id': 679
    }
    boston_celtics = {
        'sport': Sport.nba,
        'id': 680
    }
    brooklyn_nets = {
        'sport': Sport.nba,
        'id': 696
    }
    charlotte_hornets = {
        'sport': Sport.nba,
        'id': 681
    }
    chicago_bulls = {
        'sport': Sport.nba,
        'id': 682
    }
    cleveland_cavaliers = {
        'sport': Sport.nba,
        'id': 683
    }
    dallas_mavericks = {
        'sport': Sport.nba,
        'id': 684
    }
    denver_nuggets = {
        'sport': Sport.nba,
        'id': 685
    }
    detroit_pistons = {
        'sport': Sport.nba,
        'id': 686
    }
    golden_state_warriors = {
        'sport': Sport.nba,
        'id': 687
    }
    houston_rockets = {
        'sport': Sport.nba,
        'id': 688
    }
    indiana_pacers = {
        'sport': Sport.nba,
        'id': 689
    }
    los_angeles_clippers = {
        'sport': Sport.nba,
        'id': 690
    }
    los_angeles_lakers = {
        'sport': Sport.nba,
        'id': 691
    }
    memphis_grizzlies = {
        'sport': Sport.nba,
        'id': 692
    }
    miami_heat = {
        'sport': Sport.nba,
        'id': 693
    }
    milwaukee_bucks = {
        'sport': Sport.nba,
        'id': 694
    }
    minnesota_timberwolves = {
        'sport': Sport.nba,
        'id': 695
    }
    new_orleans_pelicans = {
        'sport': Sport.nba,
        'id': 697
    }
    new_york_knicks = {
        'sport': Sport.nba,
        'id': 698
    }
    oklahoma_city_thunder = {
        'sport': Sport.nba,
        'id': 699
    }
    orlando_magic = {
        'sport': Sport.nba,
        'id': 700
    }
    philadelphia_76ers = {
        'sport': Sport.nba,
        'id': 701
    }
    phoenix_suns = {
        'sport': Sport.nba,
        'id': 702
    }
    portland_trail_blazers = {
        'sport': Sport.nba,
        'id': 703
    }
    sacramento_kings = {
        'sport': Sport.nba,
        'id': 704
    }
    san_antonio_spurs = {
        'sport': Sport.nba,
        'id': 705
    }
    toronto_raptors = {
        'sport': Sport.nba,
        'id': 706
    }
    utah_jazz = {
        'sport': Sport.nba,
        'id': 707
    }
    washington_wizards = {
        'sport': Sport.nba,
        'id': 708
    }

    @staticmethod
    def value_of(sport, fan_duel_id):
        assert isinstance(sport, Sport)
        assert isinstance(fan_duel_id, int)

        for team in Team:
            if team.value['sport'] == sport and team.value['id'] == fan_duel_id:
                return team

        raise ValueError('Unable to identify team for sport: %s and id: %s', sport, fan_duel_id)


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
    }
    center = {
        'sport': Sport.nba,
        'abbreviation': 'C'
    }

    @staticmethod
    def value_of(sport, abbreviation):
        assert isinstance(sport, Sport)
        assert isinstance(abbreviation, basestring)

        for position in Position:
            if position.value['sport'] == sport and position.value['abbreviation'] == abbreviation:
                return position

        raise ValueError('Unable to identify position for sport: %s and abbreviation: %s', sport, abbreviation)


class FixtureStatus:
    def __init__(self, is_final, has_started):
        assert isinstance(is_final, bool)
        assert isinstance(has_started, bool)

        self.is_final = is_final
        self.has_started = has_started


class Fixture:
    def __init__(self, fixture_id, sport, status, away_team, home_team, start_time):
        assert isinstance(fixture_id, int)
        assert isinstance(sport, Sport)
        assert isinstance(status, FixtureStatus)
        assert isinstance(away_team, Team)
        assert isinstance(home_team, Team)
        assert isinstance(start_time, datetime)

        self.fixture_id = fixture_id
        self.sport = sport
        self.status = status
        self.away_team = away_team
        self.home_team = home_team
        self.status = status
        self.start_time = start_time


class FixturePlayerInjury:
    def __init__(self, details, status):
        assert isinstance(details, (type(None), basestring))
        assert isinstance(status, (type(None), basestring))

        self.details = details
        self.status = status


class FixturePlayer:
    def __init__(self, fixture_player_id, first_name, last_name, jersey_number, injury, is_removed, position, salary, team, fixture):
        assert isinstance(fixture_player_id, basestring)
        assert isinstance(first_name, basestring)
        assert isinstance(last_name, basestring)
        assert isinstance(jersey_number, int)
        assert isinstance(is_removed, bool)
        assert isinstance(injury, FixturePlayerInjury)
        assert isinstance(position, Position)
        assert isinstance(team, Team)
        assert isinstance(fixture, Fixture)
        assert isinstance(salary, int)

        self.fixture_player_id = fixture_player_id
        self.first_name = first_name
        self.last_name = last_name
        self.jersey_number = jersey_number
        self.injury = injury
        self.is_removed = is_removed
        self.position = position
        self.salary = salary
        self.team = team
        self.fixture = fixture
