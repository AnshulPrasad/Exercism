def flatten(iterable):
    flat_array = []
    for i in iterable:
        if i is None:
            continue
        elif type(i) is list:
            temp = flatten(i)
            flat_array.extend(temp)
        else:
            flat_array.append(i)
    return flat_array
