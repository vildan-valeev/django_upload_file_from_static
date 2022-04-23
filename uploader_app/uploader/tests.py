from django.test import TestCase

from upload_app.forms import CheckFieldsMixin


class CheckFieldsMixinTestCase(TestCase):

    def test_only_one_field(self):
        check_instance = CheckFieldsMixin()
        test_data_1 = {'from_storage': '', 'url': '', 'upload': 'text'}
        test_data_2 = {'from_storage': '', 'url': 'text', 'upload': 'text'}
        test_data_3 = {'from_storage': 'text', 'url': 'text', 'upload': 'text'}
        test_data_4 = {'from_storage': None, 'url': None, 'upload': None}
        test_data_5 = {'from_storage': 'text', 'url': None, 'upload': None}
        test_data_6 = {'from_storage': 'text', 'url': 'text', 'upload': None}
        test_data_7 = {'from_storage': '', 'url': None, 'upload': None}

        self.assertEqual(check_instance.check_fullness(test_data_1), True)
        self.assertEqual(check_instance.check_fullness(test_data_2), False)
        self.assertEqual(check_instance.check_fullness(test_data_3), False)
        self.assertEqual(check_instance.check_fullness(test_data_4), False)
        self.assertEqual(check_instance.check_fullness(test_data_5), True)
        self.assertEqual(check_instance.check_fullness(test_data_6), False)
        self.assertEqual(check_instance.check_fullness(test_data_7), False)


