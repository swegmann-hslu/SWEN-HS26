from greeting import greet


def test_einzelner_name():                       # Requirement 1
    assert greet("Bob") == "Hello, Bob."


def test_none_wird_zu_platzhalter():             # Requirement 2
    assert greet(None) == "Hello, my friend."


def test_grossbuchstaben_werden_geschrieen():    # Requirement 3
    assert greet("JERRY") == "HELLO JERRY!"


def test_zwei_namen():                           # Requirement 4
    assert greet(["Jill", "Jane"]) == "Hello, Jill and Jane."


def test_mehrere_namen_mit_oxford_komma():       # Requirement 5
    assert greet(["Amy", "Brian", "Charlotte"]) == "Hello, Amy, Brian, and Charlotte."


def test_mischung_normal_und_geschrieen():       # Requirement 6
    assert greet(["Amy", "BRIAN", "Charlotte"]) == "Hello, Amy and Charlotte. AND HELLO BRIAN!"


def test_komma_im_eintrag_wird_aufgeteilt():     # Requirement 7
    assert greet(["Bob", "Charlie, Dianne"]) == "Hello, Bob, Charlie, and Dianne."


def test_escaptes_komma_bleibt_zusammen():       # Requirement 8
    assert greet(["Bob", "\"Charlie, Dianne\""]) == "Hello, Bob and Charlie, Dianne."