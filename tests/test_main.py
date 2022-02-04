from app.main import validate_email


def test_not_english_letters():
    assert validate_email("емейл@mail.com") is False


def test_not_allowed_characters():
    assert validate_email("$mail@mail.com") is False


def test_correct_symbols():
    assert validate_email("AaBb3-8_.mail@mail.com") is True


def test_dot_symbol_is_not_first():
    assert validate_email(".alex@mail.com") is False


def test_is_rate_sign_in_right_place():
    assert validate_email("ma@il@mail.com") is False
