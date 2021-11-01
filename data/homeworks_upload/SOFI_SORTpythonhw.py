def quick_sort(sequence):
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

    return quick_sort(items_lower) + [comparison] + quick_sort(items_greater)

print(quick_sort([12,3,45,-1,2,6,4,8,14,78]))
