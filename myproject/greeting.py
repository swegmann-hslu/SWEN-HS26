def greet(name):
    """Begrüsst einen oder mehrere Namen (Greeting-Kata, Requirements 1-8)."""
    namen = _namen_aufbereiten(name)

    normale = [n for n in namen if not n.isupper()]
    geschrieene = [n for n in namen if n.isupper()]

    teile = []
    if normale:
        teile.append(f"Hello, {_namen_verbinden(normale)}.")
    if geschrieene:
        teile.append(f"HELLO {' AND '.join(geschrieene)}!")

    return " AND ".join(teile)


def _namen_aufbereiten(name):
    """Macht aus dem Parameter (None, String oder Liste) eine flache Namensliste."""
    if name is None:                 # Requirement 2
        return ["my friend"]
    if isinstance(name, str):
        elemente = [name]
    else:
        elemente = name              # Requirement 4/5: Liste

    namen = []
    for element in elemente:
        namen.extend(_element_aufteilen(element))
    return namen


def _element_aufteilen(element):
    """Teilt einen einzelnen Eintrag ggf. an Kommas auf (Requirement 7/8)."""
    # Requirement 8: in "..." eingepackte Einträge werden NICHT getrennt
    if element.startswith('"') and element.endswith('"'):
        return [element[1:-1]]
    # Requirement 7: ein normales Komma trennt mehrere Namen
    if "," in element:
        return [teil.strip() for teil in element.split(",")]
    return [element]


def _namen_verbinden(namen):
    """Verbindet normale Namen gemäss Requirement 1/4/5 (inkl. Oxford-Komma)."""
    if len(namen) == 1:
        return namen[0]
    if len(namen) == 2:
        return f"{namen[0]} and {namen[1]}"
    return ", ".join(namen[:-1]) + ", and " + namen[-1]