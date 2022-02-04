from app.main import validate_email

import pytest


@pytest.mark.parametrize(
    "email, expected",
    [
        ("mate....academy.@mate.com", False),  # 1-st bag
        (".d.e.v.my..email@dev.com", False),
        ("d.e.v.my..email@dev.com.", False),
        ("d.e.v.my.email@.dev.com", False),  # 2-nd bag
        ("d.e.v.my.email@dev.com", True),
    ],
)
def test_email_with_dots(email, expected):
    assert validate_email(email) is expected


@pytest.mark.parametrize(
    "email, expected",
    [
        ("m#te_Ac^43*my@mate.com", False),
        ("!@#$%^&*+my@dev.com", False),
    ],
)
def test_email_with_special_symbols(email, expected):
    assert validate_email(email) is expected


@pytest.mark.parametrize(
    "email, expected",
    [
        ("123456897@mate.com", True),
        ("9876543210@dev.com", True),
    ],
)
def test_email_only_with_digits(email, expected):
    assert validate_email(email) is expected


@pytest.mark.parametrize(
    "email, expected",
    [
        ("agfdsayufgsa@mate.com", True),
        ("DUYVSBFDSVFU@dev.com", True),
        ("DUYVSBFDSVFUighdfsiufds@dev.com", True),
    ],
)
def test_email_only_with_letters(email, expected):
    assert validate_email(email) is expected


@pytest.mark.parametrize(
    "email, expected",
    [
        ("my_Post_is_corRect@mate.com", True),
        ("my-post-IS_coRct@dev.com", True),
        ("MY_post-is_cor-rect@dev.com", True),
    ],
)
def test_email_with_underline_and_hyphens(email, expected):
    assert validate_email(email) is expected


@pytest.mark.parametrize(
    "email, expected",
    [
        ("Ab1-0._@mate.com", True),
        ("test_p0.t-with_All@dev.com", True),
    ],
)
def test_email_with_all_accept_symbols(email, expected):
    assert validate_email(email) is expected


@pytest.mark.parametrize(
    "email, expected",
    [
        ("Ab1-0._mate.com", False),
        ("test_p0.t-with_Alldev.com", False),
    ],
)
def test_email_without_at_sign(email, expected):
    assert validate_email(email) is expected
