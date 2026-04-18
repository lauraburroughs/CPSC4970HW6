from module4.exceptions import DuplicateEmail
from module4.identified_object import IdentifiedObject

# Laura Burroughs
# CPSC 4970
# 27 March 2026
# Project 3
# Updated for Project 6 on 14 April 2026

class Team(IdentifiedObject):

    # Properties
    @property
    def name(self):
        """Team Name"""
        return self._name

    # Added for Project 6
    @name.setter
    def name(self, value):
        """Sets the team name"""
        self._name = value

    @property
    def members(self):
        """Team Members"""
        return self._members


    # Constructor
    def __init__(self, oid, name):
        """Initializes a new Team object"""
        super().__init__(oid)
        self._name = name
        self._members = []


    # Methods
    def add_member(self, member):
        """Adds a team member to the team"""

        # Project 4 logic
        # Check for duplicate OID first
        for existing_member in self._members:
            if existing_member.oid == member.oid:
                raise DuplicateOid(member.oid)

        # Then check duplicate email with case sensitivity
        for existing_member in self._members:
            if existing_member.email.lower() == member.email.lower():
                raise DuplicateEmail(member.email)

        self._members.append(member)

    def remove_member(self, member):
        """Removes a team member from the team"""
        if member in self._members:
            self._members.remove(member)


    def member_named(self, s):
        """Checks if a team member exists"""
        for each_member in self._members:
            if each_member.name == s:
                return each_member
        return None


    def send_email(self, emailer, subject, message):
        """Sends an email to all team members"""
        recipients = [m.email for m in self._members if m.email is not None]
        emailer.send_plain_email(recipients, subject, message)


    def __str__(self):
        """Returns the team and how many members"""
        return f"{self._name}: {len(self.members)} members"