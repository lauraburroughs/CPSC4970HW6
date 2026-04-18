import unittest

from module4.team_member import TeamMember
from module4.team import Team
from module4.league import League
from module4.competition import Competition
from module4.exceptions import DuplicateEmail, DuplicateOid


# Laura Burroughs
# CPSC 4970
# 4 April 2026
# Project 4

class TestExceptions(unittest.TestCase):

    def test_duplicate_email(self):
        team = Team(1, "A")
        m1 = TeamMember(2, "Alice", "team@email.com")
        m2 = TeamMember(3, "Bob", "team@email.com")
        team.add_member(m1)
        with self.assertRaises(DuplicateEmail):
            team.add_member(m2)

    def test_case_email(self):
        team = Team(1, "A")
        m1 = TeamMember(2, "Alice", "TEAM@EMAIL.COM")
        m2 = TeamMember(3, "Bob", "team@email.com")
        team.add_member(m1)
        with self.assertRaises(DuplicateEmail):
            team.add_member(m2)

    def test_duplicate_oid(self):
        league = League(3, "League 1")
        t1 = Team(1, "A")
        t2 = Team(1, "B")
        league.add_team(t1)
        with self.assertRaises(DuplicateOid):
            league.add_team(t2)

    def test_invalid_competition(self):
        league = League(3, "League 1")
        t1 = Team(1, "A")
        t2 = Team(2, "B")
        league.add_team(t1)
        comp = Competition(5, [t2], "Chicago", "2026-04-05")
        with self.assertRaises(ValueError):
            league.add_competition(comp)

    def test_remove_team_in_competition(self):
        league = League(2, "League 1")
        t1 = Team(1, "A")
        league.add_team(t1)
        comp = Competition(5, [t1], "Chicago", "2026-04-05")
        league.add_competition(comp)
        with self.assertRaises(ValueError):
            league.remove_team(t1)
