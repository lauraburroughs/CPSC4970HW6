import yagmail

# Laura Burroughs
# CPSC 4970
# 11 April 2026
# Project 5


class Emailer:

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

    def __init__(self):
        """Initialize the Emailer instance."""
        pass

    def send_plain_email(self, recipients, subject, message):
        """Sends a real email message."""
        try:
            yag_client = yagmail.SMTP(Emailer.sender_address)
            yag_client.send(
                to=recipients,
                subject=subject,
                contents=message
            )
        except Exception as e:
            print(f"Error sending email: {e}")
