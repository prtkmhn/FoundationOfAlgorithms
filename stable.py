def stable_matching(hospitals, students):
    matches = {}
    while any(hospitals[hi] for hi in hospitals):
        for hi in hospitals:
            if hospitals[hi]:
                sj = hospitals[hi][0]
                if sj not in matches:
                    matches[sj] = hi
                    hospitals[hi].pop(0)
                else:
                    hk = matches[sj]
                    if students[sj].index(hi) < students[sj].index(hk):
                        matches[sj] = hi
                        hospitals[hi].pop(0)
                        hospitals[hk].append(sj)
    return matches




hospitals = {
    'h1': ['s1', 's2'],
    'h2': ['s3', 's4', 's5']
}

students = {
    's1': ['h1', 'h2'],
    's2': ['h2', 'h1'],
    's3': ['h2', 'h1'],
    's4': ['h2', 'h1'],
    's5': ['h2', 'h1'],
    's6': ['h2', 'h1']
}



matching = stable_matching(hospitals, students)

for s in matching:
    print(f"{s} is matched with {matching[s]}")
