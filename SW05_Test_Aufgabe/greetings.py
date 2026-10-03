def greet(name):

    # Requirement 2: Kein Name angegeben
    if name is None:
        return "Hello, my friend."

    # Mehrere Namen als Liste
    if type(name) is list:

        # Requirement 7 und 8:
        # Namen mit Komma aufteilen,
        # ausser das Komma wurde mit Anführungszeichen geschützt
        new_names = []

        for person in name:

            # Requirement 8: Geschütztes Komma
            if person.startswith("\"") and person.endswith("\""):
                new_names.append(person.strip("\""))

            # Requirement 7: Namen bei Komma aufteilen
            elif "," in person:
                split_names = person.split(",")

                for split_name in split_names:
                    new_names.append(split_name.strip())

            else:
                new_names.append(person)

        name = new_names

        # Requirement 6:
        # Normale und grossgeschriebene Namen trennen
        normal_names = []
        upper_names = []

        for person in name:
            if person.isupper():
                upper_names.append(person)
            else:
                normal_names.append(person)

        # Begrüssung für normale Namen
        normal_greeting = ""

        if len(normal_names) == 1:
            normal_greeting = "Hello, " + normal_names[0] + "."

        elif len(normal_names) == 2:
            normal_greeting = "Hello, " + normal_names[0] + " and " + normal_names[1] + "."

        elif len(normal_names) > 2:
            normal_greeting = "Hello, " + ", ".join(normal_names[:-1])
            normal_greeting += ", and " + normal_names[-1] + "."

        # Begrüssung für grossgeschriebene Namen
        upper_greeting = ""

        if len(upper_names) == 1:
            upper_greeting = "HELLO " + upper_names[0] + "!"

        # Normale und geschriene Begrüssung kombinieren
        if normal_greeting and upper_greeting:
            return normal_greeting + " AND " + upper_greeting

        if normal_greeting:
            return normal_greeting

        if upper_greeting:
            return upper_greeting

    # Requirement 3:
    # Einzelner Name komplett grossgeschrieben
    if name.isupper():
        return "HELLO " + name + "!"

    # Requirement 1:
    # Einzelner normaler Name
    return "Hello, " + name + "."