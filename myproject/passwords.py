SONDERZEICHEN = "#$!%&*?@"   # was als "special character" gilt (Requirement 5, bewusst wählbar)


def is_password_valid(password):
    """Prüft ein Passwort. True wenn gültig, sonst die Fehlermeldung(en) als String."""
    fehler = []

    if len(password) < 8:                                 # Requirement 1
        fehler.append("Password must be at least 8 characters")

    if _anzahl_ziffern(password) < 2:                     # Requirement 2
        fehler.append("The password must contain at least 2 numbers")

    if not _enthält_grossbuchstaben(password):            # Requirement 4
        fehler.append("password must contain at least one capital letter")

    if not _enthält_sonderzeichen(password):              # Requirement 5
        fehler.append("password must contain at least one special character")

    if fehler:                                            # Requirement 3: mit \n verbinden
        return "\n".join(fehler)
    return True


def _anzahl_ziffern(password):
    return sum(1 for zeichen in password if zeichen.isdigit())


def _enthält_grossbuchstaben(password):
    return any(zeichen.isupper() for zeichen in password)


def _enthält_sonderzeichen(password):
    return any(zeichen in SONDERZEICHEN for zeichen in password)