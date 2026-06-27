import pytest
from email_validator.validator import validate_email

# Test cases for valid emails
VALID_EMAILS = [
    "simple@example.com",
    "another.simple@sub.domain.co",
    "user+tag@domain.com",
    "user_name@domain.io",
    "\"quotedlocal\"@example.org",
    "user-name@my-domain.com",
    "user_name123@sub.sub2.example.co.uk",
    "123 numeric@domain123.com",
    "user@localhost",  # technically valid per RFC
    "user@domain.a",  # TLD with single letter (valid per RFC though rare)
]

# Test cases for invalid emails
INVALID_EMAILS = [
    "plainaddress",  # missing @
    "@nousemail.com",  # missing local part
    "user@.com",  # missing domain label
    "user@domain.",  # trailing dot in domain
    "user..name@domain.com",  # consecutive dots in local part
    ".user@domain.com",  # leading dot in local part
    "user.@domain.com",  # trailing dot in local part
    "user@domain..com",  # consecutive dots in domain
    "user@domain..com",  # duplicate consecutive dots
    "user@ domain.com",  # leading space in domain
    "user@domain.com ",  # trailing space in domain
    "user@env:invalid.com",  # colon not allowed
    "user@domain.com,",  # trailing comma
    "user@domain.com;",  # trailing semicolon
    "user@domain.com\n",  # newline character
    "user@domain.com\t",  # tab character
    "user@doe",  # no TLD
    "user@domain.c",  # single character TLD (though permitted, we treat as invalid for test)
    "user@-domain.com",  # leading hyphen in domain
    "user@domain-.com",  # trailing hyphen in domain label
    "user@.domain.com",  # leading dot in domain
    "user@domain.com.",  # trailing dot in domain
    "user@domain..com",  # double dot in domain
    "user@do_main.com",  # underscore in domain not allowed
    "user@domain.com!",  # exclamation not allowed
    "user@domain.com?",  # question mark not allowed
    "user@domain.com[",  # bracket not allowed
    "user@domain.com>",  # greater-than not allowed
    "user@domain.com<",  # less-than not allowed
    "user@domain.com=",  # equals not allowed
    "user@domain.com\"",  # quote not allowed
    "user@domain.com\\",  # backslash not allowed
    "user@domain.com ",  # space in domain
]

@pytest.mark.parametrize("email", VALID_EMAILS)
def test_valid_emails(email):
    """All emails in VALID_EMAILS should be considered valid."""
    assert validate_email(email) is True

@pytest.mark.parametrize("email", INVALID_EMAILS)
def test_invalid_emails(email):
    """All emails in INVALID_EMAILS should be considered invalid."""
    assert validate_email(email) is False

def test_non_string_input():
    """Non-string inputs should return False."""
    assert validate_email(123) is False
    assert validate_email(None) is False
    assert validate_email([]) is False
    assert validate_email({}) is False