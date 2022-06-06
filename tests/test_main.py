import pytest
from app.main import validate_email


@pytest.mark.parametrize("email, result",
                         [("mail1@gmail.com", True),
                          ("Мой-mail@gmail.com", False),
                          ("mail№2@gmail.com", False),
                          (".mail@gmail.com", False),
                          ("mail-gmail.com", False),
                          ("mail..@gmail.com", True),
                          ("mail$@gmail.com", False),
                          ("mail@gmail$.com", False),
                          ("mail@gmailcom", False),
                          ("mail@gmail-com", False),
                          ("mail@gmail/com", False),
                          ("mail@.gmail.com", True)])
def test_validate_email(email: str, result: bool):
    assert validate_email(email) == result
