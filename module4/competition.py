from module4.identified_object import IdentifiedObject

# Laura Burroughs
# CPSC 4970
# 27 March 2026
# Project 3

class Competition(IdentifiedObject):
    """Represents a competition between two teams."""

    # Properties
    @property
    def teams_competing(self):
        """Retrieves the teams competing this team"""
        return self._teams_competing

    @property
    def location(self):
        """Retrieves the location of this competition"""
        return self._location

    @property
    def date_time(self):
        """Retrieves the date and time of this competition"""
        return self._date_time


    # Setters
    @location.setter
    def location(self, value):
        """Sets the location of this competition"""
        self._location = value

    @date_time.setter
    def date_time(self, value):
        """Sets the date and time of this competition"""
        self._date_time = value


    # Constructor
    def __init__(self, oid, teams, location, datetime):
        """Initializes a new Competition object"""
        super().__init__(oid)
        self._teams_competing = teams
        self._location = location
        self._date_time = datetime


    # Methods
    def send_email(self, emailer, subject, message):
        """Sends the email about this competition"""
        members = set()

        for team in self._teams_competing:
            for member in team.members:
                members.add(member)

        emails = [m.email for m in members if m.email is not None]
        emailer.send_plain_email(emails, subject, message)

    def __str__(self):
        """Returns the competition name, teams, and date if applicable"""
        if self.date_time is not None:
            formatted = self.date_time.strftime("%m/%d/%Y %H:%M")
            return (f"Competition at {self.location} on {formatted} with {self._teams_competing[0].name} "
                    f"vs. {self._teams_competing[1].name}")
        else:
            return (f"Competition at {self.location} with {self._teams_competing[0].name} "
                    f"vs. {self._teams_competing[1].name}")