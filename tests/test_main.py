from app.main import validate_email


class TestValidateEmail:

    def test_should_return_false_if_use_not_English(self):
        assert validate_email('Марко@mail.com') is False

    def test_should_return_false_if_use_dots_as_first_or_last_char(self):
        assert validate_email('.test@mail.com') is False
        assert validate_email('test@mail.com.') is False

    def test_should_return_false_if_dots_come_one_after_the_other(self):
        assert validate_email('te..st@mail.com') is False # function doesn't pass this assert

    def test_should_return_false_if_at_symbol_is_not_use(self):
        assert validate_email('testmail.com') is False

    def test_return_false_when_personal_info_or_domain_start_with_dot(self):
        assert validate_email('.test@mail.com') is False
        assert validate_email('test@.mail.com') is False # function doesn't pass this assert

    def test_should_return_false_if_use_not_allowed_symbol(self): # function doesn't pass this test
        not_allowed = "! $ % & ' * + / = ? ^ { | } ~"
        for char in not_allowed:
            assert validate_email(f'te{char}st@mail.com') is False

    def test_return_false_if_double_dots_in_personal_info_part(self):
        assert validate_email('te:st@mail.com') is False
