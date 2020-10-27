from unittest import TestCase, mock
from recipes import create_recipe

name = 'name'
time = 20
link = 'www.link.se'


class TestMenu(TestCase):
    @mock.patch('builtins.input', lambda *args: '1')
    def test_main_menu(self):
        result = create_recipe(1)
        self.assertEqual(result.category, 1)
        self.assertEqual(result.name, '1')
        self.assertEqual(result.time, 1)
        self.assertEqual(result.link, '1')
