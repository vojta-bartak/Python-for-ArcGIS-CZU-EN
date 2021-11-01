def sorting(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        comparison = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > comparison:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return sorting(items_lower) + [comparison] + sorting(items_greater)

print(sorting([12,3,45,-1,2,6,4,8,14,78]))
