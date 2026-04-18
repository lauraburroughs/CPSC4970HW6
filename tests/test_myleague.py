import unittest
from module4.competition import Competition
from module4.league import League
from module4.team import Team
from module4.team_member import TeamMember
from module4.exceptions import DuplicateOid, DuplicateEmail
from datetime import datetime


# Laura Burroughs
# CPSC 4970
# 27 March 2026
# Project 3


class LeagueTests(unittest.TestCase):

    def test_create(self):
        league = League(1, "Game of Stones")
        self.assertEqual(league.oid, 1)
        self.assertEqual(league.name, "Game of Stones")
        self.assertEqual([], league.teams)
        self.assertEqual([], league.competitions)

    def test_add_team(self):
        t1 = Team(1, "Ice Man Cometh")
        league = League(1, "Game of Stones")
        league.add_team(t1)
        self.assertIn(t1, league.teams)

    def test_add_competition(self):
        league = League(1, "Game of Stones")
        dt = datetime(2026, 12, 1)
        c1 = Competition(1, [], "Athens Tournament", dt)
        league.add_competition(c1)
        self.assertIn(c1, league.competitions)

    def test_remove_team(self):
        league = League(1, "Game of Stones")
        t1 = Team(1, "Ice Man Cometh")
        league.add_team(t1)
        league.remove_team(t1)
        self.assertNotIn(t1, league.teams)

    def test_remove_team_not_in_league(self):
        league = League(1, "Game of Stones")
        t1 = Team(1, "Ice Man Cometh")
        league.remove_team(t1)
        self.assertEqual([], league.teams)

    # I updated this test to match the new project specs given in Project 4
    def test_duplicate_team_not_added(self):
        league = League(1, "Game of Stones")
        t1 = Team(1, "Ice Man Cometh")
        league.add_team(t1)
        with self.assertRaises(DuplicateOid):
            league.add_team(t1)

    # I updated this test to match the new project specs given in Project 4
    def test_duplicate_competition_not_added(self):
        league = League(1, "Game of Stones")
        dt = datetime(2026, 12, 1)
        c1 = Competition(1, [], "Athens Tournament", dt)
        league.add_competition(c1)
        with self.assertRaises(DuplicateOid):
            league.add_competition(c1)
        self.assertEqual(1, len(league.competitions))

    def test_team_named(self):
        league = League(1, "Game of Stones")
        t1 = Team(1, "Ice Man Cometh")
        league.add_team(t1)
        self.assertEqual(t1, league.team_named("Ice Man Cometh"))
        self.assertIsNone(league.team_named("Nonexistent"))

    def test_empty_league_queries(self):
        league = League(1, "Empty")
        t1 = Team(1, "Ice Man Cometh")
        m1 = TeamMember(1, "Member", "member@email.com")
        self.assertEqual([], league.teams_for_member(m1))
        self.assertEqual([], league.competitions_for_team(t1))
        self.assertEqual([], league.competitions_for_member(m1))