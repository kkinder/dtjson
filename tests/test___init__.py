import unittest
import datetime
from io import StringIO

from dtjson import loads, dumps, load, dump


class TestSerializer(unittest.TestCase):
    def setUp(self):
        self.dt1 = datetime.datetime(
            year=2000, month=5, day=1, hour=12, minute=55, second=1
        )
        self.dt2 = datetime.datetime(
            year=1950, month=5, day=1, hour=12, minute=55, second=1
        )  # Make it a long time ago
        self.ts1 = self.dt1 - self.dt2
        self.ts2 = self.dt2 - self.dt1

        self.starting_object = {
            "test_string": "hello",
            "test_dt": self.dt1,
            "test_list": ["Foo", "Bar", self.dt1, self.dt2],
            "test_dict": {"ts1": self.ts1, "ts2": self.ts2},
        }

    def test_round_trip(self):
        self.assertDictEqual(self.starting_object, loads(dumps(self.starting_object)))

    def test_roundtrip_file(self):
        fd = StringIO()
        dump(self.starting_object, fd)
        fd.seek(0)
        loaded_object = load(fd)
        self.assertDictEqual(self.starting_object, loaded_object)


if __name__ == "__main__":
    unittest.main()
