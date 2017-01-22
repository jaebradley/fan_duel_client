
# TODO: @jbradley not all fields in Contest JSON are represented - add fields as needed


class Contest:
    def __init__(self, contest_id, max_entries_per_user, name, is_guaranteed, url, entry_fee):
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
