def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    new_phrase = ""
    phrase = phrase.split(" ")
    for word in phrase:
        word = word.capitalize()
        new_phrase += word + " "
    return new_phrase