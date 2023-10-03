def oxford_comma(items):
    string = []
    for item in items:
        if len(items) == 1:
            return str(item)
        elif len(items) == 2:
            return ' and '.join(items)
        else:
            if item != items[-1]:
                string.append(item)
            else:
                string.append(f'and {item}')
                return str(', '.join(string))


