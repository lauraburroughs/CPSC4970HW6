# Laura Burroughs
# CPSC 4970
# 27 March 2026
# Project 3


class IdentifiedObject:
    """Abstract class to represent an identified object of various types."""

    @property
    def oid(self):
        """Returns the oid"""
        return self._oid

    def __init__(self, oid):
        """Initializes a new IdentifiedObject object."""
        self._oid = oid

    def __eq__(self, other):
        """Compares two IdentifiedObject objects."""
        if type(self) != type(other):
            return False
        return self.oid == other.oid

    def __hash__(self):
        """Returns a hash value based on the object's oid."""
        return hash(self.oid)

