def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    list_of_people = []
    for person in people:
        first_name = person['first']
        last_name = person['last']
        full_name = first_name + " " + last_name
        list_of_people.append(full_name)
    return list_of_people