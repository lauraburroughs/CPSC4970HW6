# Laura Burroughs
# CPSC 4970
# 4 April 2026
# Project 4

class DuplicateOid (Exception):
    def __init__(self, oid):
        super().__init__(f"Duplicate OID: {oid}")
        self.oid = oid

class DuplicateEmail (Exception):
    def __init__(self, email):
        super().__init__(f"Duplicate email: {email}")
        self.email = email