from app.main import validate_email

import pytest


class TestValidateEmail:
    @pytest.mark.parametrize(
        "email, is_valid",
        [
            pytest.param(
                "test@mail.com",
                True,
                id="Valid email"
            ),
            pytest.param(
                ".test@mail.com",
                False,
                id="Dot-first character"
            ),
            pytest.param(
                "test@mail.com.",
                False,
                id="Dot last character"
            ),
            pytest.param(
                "te$st@mai%l.com",
                False,
                id="Special character which not allowed in 'personal_info"
            ),
            pytest.param(
                "te$st@mai%l.com",
                False,
                id="Special character which not allowed in 'domain"
            ),
            pytest.param(
                "test_mail.com",
                False,
                id="Without '@'"
            ),
            pytest.param(
                "Test@mail.com",
                True,
                id="First letter uppercase"
            )
        ]
    )
    def test_validate_email(
            self,
            email,
            is_valid
    ):
        assert validate_email(email) == is_valid, f"Should return {is_valid}," \
                                                  f"when email is '{email}"
