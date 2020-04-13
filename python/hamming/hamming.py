def distance(s_a, s_b):
    if len(s_a) != len(s_b):
        raise ValueError("Length of strands not equal.")
    else:
        count = 0
        i = 0
        while len(s_a) > i:
            if s_a[i] != s_b[i]:
                count += 1
            i += 1
        return count
