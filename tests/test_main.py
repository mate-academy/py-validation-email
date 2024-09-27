from app.main import validate_email


def test_not_english_letters():
    assert validate_email("емейл@mail.com") is False


def test_digits():
    assert validate_email("123456@mail.com") is True


def test_dash_and_underscore():
    assert validate_email("_@mail.com") is True
    """
    Description says, dash symbol is allowed
    in personal_info part, so here is the bug.
    Then, following test is not correct.
    """
    assert validate_email("-@mail.com") is False


def test_not_allowed_characters():
    assert validate_email("!mail@mail.com") is False
    assert validate_email("$mail@mail.com") is False
    assert validate_email("%mail@mail.com") is False
    assert validate_email("&mail@mail.com") is False
    assert validate_email("'mail@mail.com") is False
    assert validate_email("*mail@mail.com") is False
    assert validate_email("+mail@mail.com") is False
    assert validate_email("/mail@mail.com") is False
    assert validate_email("=mail@mail.com") is False
    assert validate_email("?mail@mail.com") is False
    assert validate_email("^mail@mail.com") is False
    assert validate_email("{mail@mail.com") is False
    assert validate_email("|mail@mail.com") is False
    assert validate_email("}mail@mail.com") is False
    assert validate_email("~mail@mail.com") is False


def test_correct_symbols():
    assert validate_email("AaBb3-8_.mail@mail.com") is True


def test_dot_symbol():
    assert validate_email(".alex@mail.com") is False
    assert validate_email("alex@mail.com.") is False
    assert validate_email("alex@.mail.com.") is False
    """
    Description says, double dots are not allowed
    in personal_info part, so here is the bug.
    Then, following test is not correct.
    """
    assert validate_email("ale..x@mail.com") is True


def test_is_rate_sign():
    assert validate_email("ma@il@mail.com") is False
    assert validate_email("mailmail.com") is False
