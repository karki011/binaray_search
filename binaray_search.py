

def binaray_search(sequence, search_item):
    """will search sorted sequence and return its index """
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        # need to find the middle position of the sequence first
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]

        if midpoint_value == search_item:
            return midpoint

        elif search_item < midpoint_value:  # search left
            end_index = midpoint_value - 1

        else:
            begin_index = midpoint+1

    return None


a = [1, 2, 3, 5, 6, 7, 8, 12, 14, 15, 17, 19, 21]
b = 2
print(binaray_search(a, b))
