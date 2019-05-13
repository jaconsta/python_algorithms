def parenthesis_match(text):
    open_symbols = ('(', '{', '[')
    closing_symbols = (')', '}', ']')
    matching_symbols = dict(zip(open_symbols, closing_symbols))
    matched_text = []

    for word in text:
        if word in open_symbols:
            matched_text.append(word)
        elif word in closing_symbols:
            if matching_symbols[matched_text[-1]] == word:
                matched_text.pop()
            else:
                return False

    return len(matched_text) == 0
