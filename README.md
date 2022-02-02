# Validate email

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

Write tests for the `validate_email` function, which takes the `email` string and returns `True` for valid email, and `False` for invalid.  

An email is a string (a subset of ASCII characters) separated into two parts by `@` symbol, a "personal_info" and a domain, that is personal_info@domain.  

The personal_info part contains the following ASCII characters.  

- English letters (Aa-Zz)
- digits
- characters: - _
- character `.` ( period, dot or fullstop) provided that it is not the first or last character and it will not come one after the other.
- @ is required

- personal_info and domain can not start with dot `.`
- double dots are not allowed in personal_info part
- not allowed characters: ! $ % & ' * + / = ? ^ { | } ~

The domain name part contains letters, digits, hyphens, and dots.

The function does not check the `uniqueness` of the email (it happens during the request to DB) and the `length` of the email (it made by another function).  

Examples:
```python
validate_email('test@mail.com') is True
validate_email('t@q.c') is True
validate_email('false@email') is False
```

`Hint`: focus on the most priority and realistic cases, do not focus on edge cases.  