import json

from hello_world.formater import format_to_json
from hello_world.formater import plain_text_upper_case
import unittest


class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())

    def test_json_format(self):
        r = format_to_json("Hello World!", "Daniel")
        self.assertEqual({"imie": "Daniel", "msg": "Hello World!"},
                         json.loads(r))
