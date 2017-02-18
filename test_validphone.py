import unittest
import validphone

class TestValidPhone(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_valid_phone_num(self):
        num = "333-333-3333"
        self.assertTrue(validphone.telephone_check(num))
        num = "(123)555-5555"
        self.assertTrue(validphone.telephone_check(num))
        num = "(123) 555-5555"
        self.assertTrue(validphone.telephone_check(num))
        num = "333 333 3333"
        self.assertTrue(validphone.telephone_check(num))
        num = "3333333333"
        self.assertTrue(validphone.telephone_check(num))
        num = "1 333 333 3333"
        self.assertTrue(validphone.telephone_check(num))

    def test_letters(self):
        num = "333-abc-3333"
        self.assertFalse(validphone.telephone_check(num))

    def test_special_chars(self):
        num = "$325678908"
        self.assertFalse(validphone.telephone_check(num))

if __name__ == '__main__':
    unittest.main()
