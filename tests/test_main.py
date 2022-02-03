from app.main import validate_email

import random
import string

from app.main import validate_email

import pytest


def email_generator():
    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    numbers = string.digits
    dot = "."
    hyphens = "-"
    underlining = "_"

    length_pi = random.randint(8, 16)

    all_symbols = [letters_upper, letters_lower, numbers, dot, hyphens, underlining]
    personal_info = ""
    domain_before_dot = ""
    domain_after_dot = ""

    personal_info += random.choice(letters_upper)
    personal_info += random.choice(letters_lower)
    personal_info += random.choice(numbers)
    personal_info += random.choice(dot)
    personal_info += random.choice(hyphens)
    personal_info += random.choice(underlining)

    while len(personal_info) < length_pi:
        personal_info += random.choice(all_symbols[random.randint(0, 5)])

    length_domain = random.randint(3, 6)

    domain_before_dot += random.choice(letters_lower)
    domain_after_dot += random.choice(letters_lower)

    while len(domain_before_dot) < length_domain:
        domain_before_dot += random.choice(letters_lower[random.randint(0, 25)])

    while len(domain_after_dot) < length_domain:
        domain_after_dot += random.choice(letters_lower[random.randint(0, 25)])

    random_email = personal_info + "@" + domain_before_dot + "." + domain_after_dot

    return random_email


@pytest.mark.parametrize(
    "email, expected",
    [
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
        (email_generator(), True),
    ],
)
def test_random_email_generator(email, expected):
    assert validate_email(email) is expected
