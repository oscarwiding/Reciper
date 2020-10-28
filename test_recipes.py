from unittest import TestCase, mock
from recipes import create_recipe

name = 'name'
time = '20'
link = 'www.link.se'


class TestMenu(TestCase):
    @mock.patch('builtins.input', side_effect=[name, time, link])
    def test_main_menu(self, _):
        result = create_recipe(1)
        self.assertEqual(result.category, 1)
        self.assertEqual(result.name, name)
        self.assertEqual(result.time, int(time))
        self.assertEqual(result.link, link)
