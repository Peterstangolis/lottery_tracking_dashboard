

def list_of_nums(start, stop, selections, lines):
    from random import choice

    lines_played = dict()
    for l in range(lines):
        #print(f"Line_{l}")
        nums = list()
        for i in range(selections+1):
            n = choice([i for i in range(start,stop) if i not in nums])
            nums.append(n)
        lines_played[f"Line_{l+1}"] = nums
    return lines_played