from pytz import utc
from datetime import datetime

from data.models import Contest, FixtureListStatus, FixtureList, Sport, Team, Fixture, FixturePlayer,\
    FixturePlayerInjury, Position


class ContestsDeserializer:
    contests_field_name = 'contests'

    def __init__(self):
        pass

    @staticmethod
    def deserialize(contests_json):
        assert ContestsDeserializer.contests_field_name in contests_json

        return [ContestDeserializer.deserialize(contest_json=contest)
                for contest in contests_json[ContestsDeserializer.contests_field_name]]


class ContestDeserializer:
    contest_id_field_name = 'id'
    max_entries_per_user_field_name = 'max_entries_per_user'
    name_field_name = 'name'
    is_guaranteed_field_name = 'guaranteed'
    url_field_name = '_url'
    entry_fee_field_name = 'entry_fee'

    def __init__(self):
        pass

    @staticmethod
    def deserialize(contest_json):
        assert ContestDeserializer.contest_id_field_name in contest_json
        assert ContestDeserializer.max_entries_per_user_field_name in contest_json
        assert ContestDeserializer.name_field_name in contest_json
        assert ContestDeserializer.is_guaranteed_field_name in contest_json
        assert ContestDeserializer.url_field_name in contest_json
        assert ContestDeserializer.entry_fee_field_name in contest_json

        return Contest(contest_id=contest_json[ContestDeserializer.contest_id_field_name],
                       max_entries_per_user=contest_json[ContestDeserializer.max_entries_per_user_field_name],
                       name=contest_json[ContestDeserializer.name_field_name],
                       is_guaranteed=contest_json[ContestDeserializer.is_guaranteed_field_name],
                       url=contest_json[ContestDeserializer.url_field_name],
                       entry_fee=contest_json[ContestDeserializer.entry_fee_field_name])


class FixtureStatusDeserializer:
    has_started_field_name = 'started'
    is_final_field_name = 'final'

    def __init__(self):
        pass

    @staticmethod
    def deserialize(fixture_status_json):
        assert FixtureStatusDeserializer.has_started_field_name in fixture_status_json
        assert FixtureStatusDeserializer.is_final_field_name in fixture_status_json

        return FixtureListStatus(has_started=fixture_status_json[FixtureStatusDeserializer.has_started_field_name],
                                 is_final=fixture_status_json[FixtureStatusDeserializer.is_final_field_name])


class FixtureListsDeserializer:
    fixtures_field_name = 'fixture_lists'

    def __init__(self):
        pass

    @staticmethod
    def deserialize(fixture_lists_json):
        assert FixtureListsDeserializer.fixtures_field_name in fixture_lists_json

        return [FixtureListDeserializer.deserialize(fixture_list_json=fixture)
                for fixture in fixture_lists_json[FixtureListsDeserializer.fixtures_field_name]]


class FixtureListDeserializer:
    fixture_id_field_name = 'id'
    url_field_name = '_url'
    status_field_name = 'status'
    start_time_field_name = 'start_date'
    players_field_name = 'players'
    players_url_field_name = '_url'
    sport_field_name = 'sport'
    salary_cap_field_name = 'salary_cap'

    start_time_timezone = utc
    start_time_format = '%Y-%m-%dT%H:%M:%SZ'

    def __init__(self):
        pass

    @staticmethod
    def deserialize(fixture_list_json):
        assert FixtureListDeserializer.fixture_id_field_name in fixture_list_json
        assert FixtureListDeserializer.url_field_name in fixture_list_json
        assert FixtureListDeserializer.status_field_name in fixture_list_json
        assert FixtureListDeserializer.start_time_field_name in fixture_list_json
        assert FixtureListDeserializer.players_field_name in fixture_list_json
        assert FixtureListDeserializer.players_url_field_name in fixture_list_json[FixtureListDeserializer.players_field_name]
        assert FixtureListDeserializer.sport_field_name in fixture_list_json
        assert FixtureListDeserializer.salary_cap_field_name in fixture_list_json

        return FixtureList(fixture_id=fixture_list_json[FixtureListDeserializer.fixture_id_field_name],
                           url=fixture_list_json[FixtureListDeserializer.url_field_name],
                           status=FixtureStatusDeserializer.deserialize(fixture_status_json=fixture_list_json[FixtureListDeserializer.status_field_name]),
                           start_time=FixtureListDeserializer.deserialize_start_time(start_time=fixture_list_json[FixtureListDeserializer.start_time_field_name]),
                           players_url=fixture_list_json[FixtureListDeserializer.players_field_name][FixtureListDeserializer.players_url_field_name],
                           sport=Sport.value_of(name=fixture_list_json[FixtureListDeserializer.sport_field_name]),
                           salary_cap=fixture_list_json[FixtureListDeserializer.salary_cap_field_name])

    @staticmethod
    def deserialize_start_time(start_time):
        assert isinstance(start_time, basestring)

        deserialized_start_time = datetime.strptime(start_time, FixtureListDeserializer.start_time_format)
        return utc.localize(deserialized_start_time)


class FixturePlayerDeserializer:
    fixture_player_id_field_name = 'id'
    first_name_field_name = 'first_name'
    last_name_field_name = 'last_name'
    jersey_number_field_name = 'jersey_number'
    injury_details_field_name = 'injury_details'
    injury_status_field_name = 'injury_status'
    fixture_field_name = 'fixture'
    fixture_members_field_name = '_members'
    is_removed_field_name = 'removed'
    position_field_name = 'position'
    salary_field_name = 'salary'
    team_field_name = 'team'
    team_member_field_name = '_members'

    def __init__(self):
        pass

    @staticmethod
    def deserialize(fixture_player_json, fixtures_mapping):
        assert FixturePlayerDeserializer.fixture_player_id_field_name in fixture_player_json
        assert FixturePlayerDeserializer.first_name_field_name in fixture_player_json
        assert FixturePlayerDeserializer.last_name_field_name in fixture_player_json
        assert FixturePlayerDeserializer.jersey_number_field_name in fixture_player_json
        assert FixturePlayerDeserializer.injury_details_field_name in fixture_player_json
        assert FixturePlayerDeserializer.fixture_field_name in fixture_player_json
        assert FixturePlayerDeserializer.fixture_members_field_name in fixture_player_json[FixturePlayerDeserializer.fixture_field_name]
        assert FixturePlayerDeserializer.is_removed_field_name in fixture_player_json
        assert FixturePlayerDeserializer.position_field_name in fixture_player_json
        assert FixturePlayerDeserializer.salary_field_name in fixture_player_json
        assert FixturePlayerDeserializer.team_field_name in fixture_player_json
        assert FixturePlayerDeserializer.team_member_field_name in fixture_player_json[FixturePlayerDeserializer.team_field_name]

        fixture_members = fixture_player_json[FixturePlayerDeserializer.fixture_field_name][FixturePlayerDeserializer.fixture_members_field_name]
        assert isinstance(fixture_members, list)
        assert len(fixture_members) == 1

        fixture_id = int(fixture_members[0])
        fixture = fixtures_mapping.get(fixture_id)
        assert isinstance(fixture, Fixture)

        team_members = fixture_player_json[FixturePlayerDeserializer.team_field_name][FixturePlayerDeserializer.team_member_field_name]
        assert isinstance(team_members, list)
        assert len(team_members) == 1

        team_id = int(team_members[0])
        team = Team.value_of(sport=fixture.sport, fan_duel_id=team_id)

        injury = FixturePlayerInjury(status=fixture_player_json[FixturePlayerDeserializer.injury_status_field_name],
                                     details=fixture_player_json[FixturePlayerDeserializer.injury_details_field_name])

        return FixturePlayer(fixture_player_id=fixture_player_json[FixturePlayerDeserializer.fixture_player_id_field_name],
                             first_name=fixture_player_json[FixturePlayerDeserializer.first_name_field_name],
                             last_name=fixture_player_json[FixturePlayerDeserializer.last_name_field_name],
                             jersey_number=fixture_player_json[FixturePlayerDeserializer.jersey_number_field_name],
                             injury=injury,
                             is_removed=fixture_player_json[FixturePlayerDeserializer.is_removed_field_name],
                             position=Position.value_of(sport=fixture.sport,
                                                        abbreviation=fixture_player_json[FixturePlayerDeserializer.position_field_name]),
                             salary=fixture_player_json[FixturePlayerDeserializer.salary_field_name],
                             team=team,
                             fixture=fixture)
