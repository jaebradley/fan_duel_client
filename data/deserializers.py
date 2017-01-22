from data.models import Contest


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
    name_field_name  = 'name'
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

