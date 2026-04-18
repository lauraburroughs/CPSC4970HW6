import unittest
import os
from module4.league import League
from module5.league_database import LeagueDatabase
from module4.team import Team
from module4.team_member import TeamMember

# Laura Burroughs
# CPSC 4970
# 10 April 2026
# Project 5

class TestLeagueDatabase(unittest.TestCase):

    def setUp(self):
        LeagueDatabase._sole_instance = None
        self.db = LeagueDatabase.instance()

    def test_instance_singleton(self):
        db1 = LeagueDatabase.instance()
        db2 = LeagueDatabase.instance()
        self.assertIs(db1, db2)

    def test_add_league(self):
        league = League(self.db.next_oid(), "Game of Stones")
        self.db.add_league(league)
        self.assertIn(league, self.db.leagues)

    def test_league_named_object(self):
        league = League(self.db.next_oid(), "Game of Stones")
        self.db.add_league(league)
        result = self.db.league_named("GaMe Of StOnEs")
        self.assertIs(result, league)

    def test_remove_league_exists(self):
        league = League(self.db.next_oid(), "Game of Stones")
        self.db.add_league(league)
        self.db.remove_league(league)
        self.assertNotIn(league, self.db.leagues)

    def test_remove_league_not_exists(self):
        league1 = League(self.db.next_oid(), "Game of Stones")
        league2 = League(self.db.next_oid(), "Icebreakers")
        self.db.add_league(league1)
        self.db.remove_league(league2)
        self.assertIn(league1, self.db.leagues)
        self.assertNotIn(league2, self.db.leagues)

    def test_next_oid(self):
        first_oid = self.db.next_oid()
        second_oid = self.db.next_oid()
        third_oid = self.db.next_oid()
        self.assertEqual(first_oid, 1)
        self.assertEqual(second_oid, 2)
        self.assertEqual(third_oid, 3)

    def test_save_and_load(self):
        # set it up
        file_name = "test.db.pkl"
        league = League(self.db.next_oid(), "Game of Stones")
        self.db.add_league(league)
        self.db.save(file_name)

        # reset and load
        LeagueDatabase._sole_instance = None
        LeagueDatabase.load(file_name)
        db2 = LeagueDatabase.instance()
        result = db2.league_named("Game of Stones")

        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Game of Stones")
        os.remove(file_name)

    def test_load_backup_fallback(self):
        # set it up
        file_name = "test_db.pkl"
        backup_file = file_name + ".backup"
        league = League(self.db.next_oid(), "Backup League")
        self.db.add_league(league)
        self.db.save(file_name)

        # simulate missing main file
        os.rename(file_name, backup_file)
        LeagueDatabase._sole_instance = None
        LeagueDatabase.load(file_name)
        db2 = LeagueDatabase.instance()
        result = db2.league_named("Backup League")

        self.assertIsNotNone(result)
        os.remove(backup_file)

    def test_import_league_teams(self):
        file_name = "test_import.csv"

        # create a sample CSV
        with open(file_name, "w", encoding="utf-8", newline="") as f:
            f.write("Team name,Member name,Member email\n")
            f.write("Team A,John Doe,john@example.com\n")
            f.write("Team A,Jane Smith,jane@example.com\n")

        league = League(self.db.next_oid(), "Import League")
        self.db.import_league_teams(league, file_name)

        self.assertEqual(len(league.teams), 1)
        team = league.teams[0]
        self.assertEqual(len(team.members), 2)
        os.remove(file_name)

    def test_export_league_teams(self):
        file_name = "test_export.csv"
        league = League(self.db.next_oid(), "Export League")
        team = Team(self.db.next_oid(), "Team A")
        league.add_team(team)
        member = TeamMember(self.db.next_oid(), "John Doe", "john@example.com")
        team.add_member(member)
        self.db.export_league_teams(league, file_name)

        with open(file_name, "r", encoding="utf-8") as f:
            lines = f.readlines()

        self.assertTrue(len(lines) >= 2)  # header + at least one row
        self.assertIn("Team name,Member name,Member email", lines[0])
        os.remove(file_name)









