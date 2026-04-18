import unittest
from module5.emailer import Emailer

# Laura Burroughs
# CPSC 4970
# 11 April 2026
# Project 5

class TestEmailer(unittest.TestCase):

    def setUp(self):
        Emailer._sole_instance = None
        Emailer.configure("testsender@gmail.com")
        self.emailer = Emailer.instance()

    def test_singleton(self):
        e1 = Emailer.instance()
        e2 = Emailer.instance()
        self.assertIs(e1, e2)

    def test_configure(self):
        self.assertEqual(Emailer.sender_address, "testsender@gmail.com")

    def test_send_plain_email_runs(self):
        try:
            self.emailer.send_plain_email(
                recipients=["fake@example.com"],
                subject="Test",
                message="Hello"
            )
        except Exception:
            self.fail("send_plain_email raised an exception")