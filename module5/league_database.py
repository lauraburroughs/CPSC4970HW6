import os
import pickle
import csv
from module4.team import Team
from module4.team_member import TeamMember


# Laura Burroughs
# CPSC 4970
# 9 April 2026
# Project 5


class LeagueDatabase:

    _sole_instance = None

    @classmethod
    def instance(cls):
        """Get the instance of the LeagueDatabase class"""
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    def __init__(self):
        """Initialize the LeagueDatabase class"""
        self._leagues = []
        self._last_oid = 0

    @property
    def leagues(self):
        """Get the list of leagues"""
        return list(self._leagues)

    def add_league(self, league):
        """Add a league to the database, not checking for dupes according to the spec"""
        self._leagues.append(league)

    def remove_league(self, league):
        """Remove a league to the database, not checking for dupes according to the spec"""
        if league in self._leagues:
            self._leagues.remove(league)

    def league_named(self, name):
        """Get the league with the given name"""
        name = name.lower()
        for league in self._leagues:
            if league.name.lower() == name:
                return league
        return None

    def next_oid(self):
        """Get the next oid of the league"""
        self._last_oid = self._last_oid + 1
        return self._last_oid

    def save(self, file_name):
        """Save the league to the file"""
        if os.path.exists(file_name):
            os.rename(file_name, file_name + ".backup")
        with open(file_name, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, file_name):
        """Load the league from the file"""
        try:
            with open(file_name, "rb") as f:
                cls._sole_instance = pickle.load(f)

        except Exception:
            print("Error loading database file. Trying backup.")
            backup_file = file_name + ".backup"

            try:
                with open(backup_file, "rb") as f:
                    cls._sole_instance = pickle.load(f)
            except Exception:
                print("Error loading backup file. Backup also failed.")
                cls._sole_instance = None

    def import_league_teams(self, league, file_name):
        """Load teams and members from the CSV file into a league"""

        try:
            with open(file_name, "r", encoding="utf-8", newline="") as f:
                reader = csv.reader(f)

                next(reader)            # skips the header row

                for row in reader:
                    if len(row) < 3:
                        continue        # skips weird rows

                    team_name, member_name, member_email = row

                    # find or create a team
                    team = league.team_named(team_name)
                    if team is None:
                        team = Team(self.next_oid(), team_name)
                        league.add_team(team)

                    # create a member
                    member = TeamMember(
                        self.next_oid(),
                        member_name,
                        member_email
                    )

                    # add to a team (reminder that Team handles dupes)
                    team.add_member(member)

        except Exception:
            print("Error loading league from CSV file.")

    def export_league_teams(self, league, file_name):
        """Write a league's teams and members to the CSV file"""

        try:
            with open(file_name, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)

                # header row
                writer.writerow(["Team name", "Member name", "Member email"])

                # data rows
                for team in league.teams:
                    for member in team.members:
                        writer.writerow([
                            team.name,
                            member.name,
                            member.email
                        ])

        except Exception:
            print("Error writing league to the CSV file.")

