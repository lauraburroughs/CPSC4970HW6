from module4.identified_object import IdentifiedObject

# Laura Burroughs
# CPSC 4970
# 27 March 2026
# Project 3


class TeamMember(IdentifiedObject):
    """Represents an individual team member"""

    # Properties
    @property
    def name(self):
        """Retrieves the name of the team member"""
        return self._name

    @property
    def email(self):
        """Retrieves the email of the team member"""
        return self._email


    # Setters
    @name.setter
    def name(self, value):
        """Sets the name of the team member"""
        self._name = value

    @email.setter
    def email(self, value):
        """Sets the email of the team member"""
        self._email = value



    # Constructor
    def __init__(self, oid, name, email):
        """Initializes a new TeamMember object"""
        super().__init__(oid)
        self.name = name
        self.email = email


    # Methods
    def send_email(self, emailer, subject, message):
        """Sends an email to the team member"""
        if self.email is None:
            return
        emailer.send_plain_email([self.email], subject, message)

    def __str__(self):
        """Returns the team member and their email"""
        return f"{self.name}<{self.email}>"






