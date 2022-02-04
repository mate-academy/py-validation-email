import pytest

from app.main import validate_email


@pytest.mark.parametrize(
    "email,result", [
        ("ABCDEfghij@mail.com", True),
        ("1234567890@my-mail.com", True)
    ]
)
def test_should_check_english_letters_and_digits_in_email(email, result):
    assert validate_email(email) is result


@pytest.mark.parametrize(
    "email,result", [
        (".wrong@mail.com", False),
        ("wrongadress.@mail.com", False),  # this test has failed
        ("wrong..adress@mail.com", False),  # this test has failed
        ("wrongadress@.mail.com", False),  # this test has failed
        ("my.correct.adress@mail.com", True)
    ]
)
def test_should_check_correct_dots_in_email(email, result):
    assert validate_email(email) is result


@pytest.mark.parametrize(
    "email,result", [
        ("wrong_mail.com", False),
        ("correct.adress@mail.com", True)
    ]
)
def test_should_check_dog_symbol_in_email(email, result):
    assert validate_email(email) is result


@pytest.mark.parametrize(
    "email,result", [
        ("!$%&'*+/=?^:{|}~@mail.com", False),
        ("wrong_mail@my_mail#com&", False),
        ("my_correct-adress@my-mail.com", True)
    ]
)
def test_should_check_special_characters_in_email(email, result):
    assert validate_email(email) is result
