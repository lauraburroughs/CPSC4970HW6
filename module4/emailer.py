# Laura Burroughs
# CPSC 4970
# 27 March 2026
# Project 3

class Emailer:
    """Class to represent an email address."""

    # Variables
    sender_address = None
    _sole_instance = None


    # Methods
    @classmethod
    def configure(cls, sender_address):
        """Configures the email sender address."""
        cls.sender_address = sender_address

    @classmethod
    def instance(cls):
        """Returns the Emailer instance."""
        if cls._sole_instance is None:
            cls._sole_instance = Emailer()
        return cls._sole_instance


    # Instance Method
    def send_plain_email(self, recipients, subject, message):
        """Sends the plain email message."""
        for recipient in recipients:
            print(f"Sending mail to: {recipient}")