import module4.competition
from module4.exceptions import DuplicateOid
from module4.identified_object import IdentifiedObject
from module4.team_member import TeamMember
from module4.team import Team
from module4.competition import Competition

# Laura Burroughs
# CPSC 4970
# 27 March 2026
# Project 3
# Updated for Project 6 on 14 April 2026


class League(IdentifiedObject):
    """Represents a league"""

    # Properties
    @property
    def name(self):
        """Name of the league"""
        return self._name

    # Added for Project 6
    @name.setter
    def name(self, value):
        """Sets the name of the league"""
        self._name = value

    @property
    def teams(self):
        """List of all teams this league"""
        return self._teams

    @property
    def competitions(self):
        """List of all competitions this league"""
        return self._competitions


    # Constructor
    def __init__(self, oid, name):
        """Initializes a new League object"""
        super().__init__(oid)
        self._name = name
        self._teams = []
        self._competitions = []


    # Methods
    def add_team(self, team):
        """Adds a new team to this league"""

        # Project 4 logic
        for existing_team in self._teams:
            if existing_team.oid == team.oid:
                raise DuplicateOid(team.oid)

        self._teams.append(team)

    def remove_team(self, team):
        """Removes a team from this league"""

        # Project 4 logic
        for competition in self._competitions:
            if team in competition.teams_competing:
                raise ValueError()

        if team in self._teams:
            self._teams.remove(team)

    def team_named(self, team_name):
        """Checks if a team exists in this league"""
        for each_team in self._teams:
            if each_team.name == team_name:
                return each_team
        return None

    def add_competition(self, competition):
        """Adds a new competition to this league"""

        # Project 4 logic
        # Prevent duplicates by OID
        for existing in self._competitions:
            if existing.oid == competition.oid:
                raise DuplicateOid(competition.oid)

        # All teams must be in the league
        for team in competition.teams_competing:
            if team not in self._teams:
                raise ValueError
        self._competitions.append(competition)

    def teams_for_member(self, member):
        """Returns a list of all teams a member plays on"""
        result = []
        for team in self._teams:
            if member in team.members:
                result.append(team)
        return result

    def competitions_for_team(self, team):
        """Returns a list of all competitions in which team is participating"""
        result = []
        for comp in self._competitions:
            if team in comp.teams_competing:
                result.append(comp)
        return result

    def competitions_for_member(self, member):
        """Returns a list of all competitions in which member plays on"""
        result = []
        for comp in self._competitions:
            for team in comp.teams_competing:
                if member in team.members:
                    result.append(comp)
                    break
        return result

    def __str__(self):
        """Returns the league's name, teams, and competitions"""
        return f"{self._name}: {len(self._teams)} teams, {len(self._competitions)} competitions"

