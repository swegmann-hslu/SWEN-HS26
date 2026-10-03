from greetings import greet

def test_greet_bob():
    assert greet("Bob") == "Hello, Bob."

def test_greet_none():
    assert greet(None) == "Hello, my friend."

def test_greet_uppercase():
    assert greet("JERRY") == "HELLO JERRY!"

def test_greet_two_names():
    assert greet(["Jill", "Jane"]) == "Hello, Jill and Jane."

def test_greet_multiple_names():
    assert greet(["Amy", "Brian", "Charlotte"]) == "Hello, Amy, Brian, and Charlotte."

def test_greet_mixed_names():
    assert greet(["Amy", "BRIAN", "Charlotte"]) == "Hello, Amy and Charlotte. AND HELLO BRIAN!"

def test_greet_names_with_comma():
    assert greet(["Bob", "Charlie, Dianne"]) == "Hello, Bob, Charlie, and Dianne."

def test_greet_escaped_comma():
    assert greet(["Bob", "\"Charlie, Dianne\""]) == "Hello, Bob and Charlie, Dianne."