import unittest
from module4.team_member import TeamMember
from module4.team import Team

# Laura Burroughs
# CPSC 4970
# 27 March 2026
# Project 3


class fakeEmailer:
    def __init__(self):
        self.sent = None

    def send_plain_email(self, recipients, subject, message):
        self.sent = (recipients, subject, message)


class TestTeam(unittest.TestCase):

    # Making a team member
    def test_constructor(self):
        m = TeamMember(1, "Alice", "alice@email.com")
        self.assertEqual(m.name, "Alice")
        self.assertEqual(m.email, "alice@email.com")
        self.assertEqual(m.oid, 1)

    def test_setters(self):
        m = TeamMember(1, "Alice", "alice@email.com")
        m.name = "Bob"
        self.assertEqual(m.name, "Bob")
        m.email = "bob@email.com"
        self.assertEqual(m.email, "bob@email.com")


    # Team add/remove/check
    def test_add_member(self):
        t = Team(1, "Engineering")
        m = TeamMember(2, "Alice", "alice@email.com")
        t.add_member(m)
        self.assertIn(m, t.members)

    # Commented out to update for Project 4
    # def test_add_duplicate_member(self):
    #     t = Team(1, "Engineering")
    #     m = TeamMember(2, "Alice", "alice@email.com")
    #     t.add_member(m)
    #     t.add_member(m)
    #     self.assertEqual(len(t.members), 1)

    def test_remove_member(self):
        t = Team(1, "Engineering")
        m = TeamMember(2, "Alice", "alice@email.com")
        t.add_member(m)
        t.remove_member(m)
        self.assertNotIn(m, t.members)

    def test_member_named(self):
        t = Team(1, "Engineering")
        m1 = TeamMember(2, "Alice", "alice@email.com")
        m2 = TeamMember(3, "Bob", "bob@email.com")
        t.add_member(m1)
        t.add_member(m2)
        self.assertEqual(t.member_named("Alice"), m1)
        self.assertEqual(t.member_named("Bob"), m2)
        self.assertIsNone(t.member_named("Charlie"))


    # Email
    def test_send_plain_email(self):
        m = TeamMember(1, "Alice", "alice@email.com")
        fake = fakeEmailer()
        m.send_email(fake, "Hello", "Test message")
        self.assertIsNotNone(fake.sent)
        self.assertEqual(fake.sent[0], ["alice@email.com"])




