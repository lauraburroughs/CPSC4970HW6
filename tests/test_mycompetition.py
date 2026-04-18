import unittest
from module4.competition import Competition
from module4.team import Team
from module4.team_member import TeamMember
from datetime import datetime


# Laura Burroughs
# CPSC 4970
# 27 March 2026
# Project 3


class fakeEmailer:
    def __init__(self):
        self.sent = None

    def send_plain_email(self, recipients, subject, message):
        self.sent = (recipients, subject, message)



class CompetitionTest(unittest.TestCase):
    """Represents a competition between two teams."""

    # Constructor test
    def test_constructor(self):
        team1 = Team(1, "A")
        team2 = Team(2, "B")
        dt = datetime(2026, 12, 1, 19, 30)
        comp = Competition(10, [team1, team2], "Chicago", dt)
        self.assertEqual(comp.oid, 10)
        self.assertEqual(comp.location, "Chicago")
        self.assertEqual(comp.teams_competing, [team1, team2])
        self.assertEqual(comp.date_time, dt)


    # Email tests
    def test_send_email(self):
        fake = fakeEmailer()

        team1 = Team(1, "A")
        m1 = TeamMember(2, "Alice", "alice@email.com")
        m2 = TeamMember(3, "Bob", "bob@email.com")
        team1.add_member(m1)
        team1.add_member(m2)

        team2 = Team(2, "B")
        m3 = TeamMember(5, "Charlie", "charlie@email.com")
        m4 = TeamMember(6, "David", "david@email.com")
        team2.add_member(m3)
        team2.add_member(m4)

        comp = Competition(10, [team1, team2], "Chicago", None)
        comp.send_email(fake, "Hello", "Test")
        self.assertIsNotNone(fake.sent)
        self.assertEqual(len(fake.sent[0]), 4)


    def test_same_member(self):
        fake = fakeEmailer()

        team1 = Team(1, "A")
        team2 = Team(2, "B")
        m1 = TeamMember(3, "Alice", "alice@email.com")
        team1.add_member(m1)
        team2.add_member(m1)

        comp = Competition(10, [team1, team2], "Chicago", None)
        comp.send_email(fake, "Hello", "Test")
        self.assertEqual(len(fake.sent[0]), 1)








