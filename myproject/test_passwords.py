from passwords import is_password_valid


def test_gueltiges_passwort_gibt_true():
    assert is_password_valid("Abcdef12!") is True


def test_zu_kurz():                                       # Requirement 1
    assert "Password must be at least 8 characters" in is_password_valid("Ab1!")


def test_zu_wenig_ziffern():                              # Requirement 2
    assert "The password must contain at least 2 numbers" in is_password_valid("Abcdefg!")


def test_fehlender_grossbuchstabe():                      # Requirement 4
    assert "password must contain at least one capital letter" in is_password_valid("abcdef12!")


def test_fehlendes_sonderzeichen():                       # Requirement 5
    assert "password must contain at least one special character" in is_password_valid("Abcdef123")


def test_mehrere_fehler_mit_zeilenumbruch():              # Requirement 3
    # "somepw": zu kurz, keine 2 Ziffern, kein Grossbuchstabe, kein Sonderzeichen
    assert is_password_valid("somepw") == (
        "Password must be at least 8 characters\n"
        "The password must contain at least 2 numbers\n"
        "password must contain at least one capital letter\n"
        "password must contain at least one special character"
    )