import pytest
from check_password import check_password_strength


@pytest.mark.parametrize(
    "password,username,min_length,require_uppercase,require_numbers,require_special,expected_overall_valid,expected_strength",
    [
        ("Abc123!", "user", 6, True, True, True, True, "strong"),
        ("Abc123",  "user", 6, True, True, True, False, "strong"),
        ("user123!","user", 6, True, True, True, False, "strong"),
        ("Abc",     "user", 6, True, False, False, False, "medium"),
        ("a",       "user", 6, False, False, False, False, "weak"),
    ]
)
def test_valid_scenarios(password, username, min_length, require_uppercase,
                         require_numbers, require_special,
                         expected_overall_valid, expected_strength):
    result = check_password_strength(password, username, min_length,
                                     require_uppercase, require_numbers, require_special)
    assert result["overall_valid"] == expected_overall_valid
    assert result["strength"] == expected_strength


@pytest.mark.parametrize(
    "min_length,expected_length_ok",
    [
        (5, False),
        (6, True),
        (7, True),
        (19, True),
        (20, True),
        (21, True),
    ]
)
def test_boundary_min_length(min_length, expected_length_ok):
    password = "12345678901234567890"
    result = check_password_strength(password, "user", min_length, False, False, False)
    assert result["length_ok"] == expected_length_ok


def test_empty_password():
    result = check_password_strength("", "user", 6, False, False, False)
    assert result["length_ok"] is False
    assert result["strength"] == "weak"


def test_empty_username():
    result = check_password_strength("Abc123!", "", 6, True, True, True)
    assert result["no_username_ok"] is True
    assert result["overall_valid"] is True


@pytest.mark.parametrize(
    "require_numbers,password,expected_numbers_ok",
    [
        (False, "Abcdef!", True),
        (False, "Abc123!", True),
    ]
)
def test_require_numbers_false_handling(require_numbers, password, expected_numbers_ok):
    result = check_password_strength(password, "user", 6, True, require_numbers, True)
    assert result["numbers_ok"] == expected_numbers_ok


def test_overall_valid_with_numbers_not_required():
    result = check_password_strength("Abcdef!", "user", 6, True, False, True)
    assert result["overall_valid"] is True

if __name__ == "__main__":
    pytest.main(["-v", __file__])