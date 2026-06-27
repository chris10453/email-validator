import re

# Simple regex for email validation that covers most RFC 5322 cases without being overly strict.
# This pattern matches typical email formats, including plus addressing and quoted local parts.
EMAIL_REGEX = re.compile(
    r"^(?P<local>[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+"
    r"(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*"
    r"|(?:\"[^\"]\")+)"
    r"@"
    r"(?P<domain>(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})$"
)

def validate_email(email: str) -> bool:
    """
    Validate an email address.
    
    This function checks for a valid local-part and domain portion.
    It supports:
    - Alphanumeric characters, and allowed special characters in the local part.
    - Dotted segments in the local part.
    - Quoted strings in the local part.
    - Domain names with one or more labels separated by dots.
    - Top-level domains of at least two letters.
    
    Args:
        email: The email address to validate.
        
    Returns:
        True if the email appears valid, False otherwise.
    """
    if not isinstance(email, str):
        return False
    email = email.strip()
    if not email:
        return False
    return bool(EMAIL_REGEX.fullmatch(email))