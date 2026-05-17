import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        self.assertIn(", ".join(SUPPORTED), rv.get_data(as_text=True))

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEqual(
            {"imie": "Daniel", "msg": "Hello World!"},
            rv.get_json(),
        )
