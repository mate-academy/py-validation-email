import re


def validate_email(email: str) -> bool:
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{1,}\b'
    return re.fullmatch(email_regex, email) is not None
