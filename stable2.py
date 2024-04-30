def stable_matching(hospitals, students, hospital_free_positions):
    """
    This function takes a dictionary of hospitals, a dictionary of students,
    and a dictionary of free hospital positions, and returns a stable matching
    of hospitals and students.
    """
    for h in hospitals:
        if hospital_free_positions[h] > 0:
            for s in hospitals[h]:
                if s not in students:
                    students[s] = h
                    hospital_free_positions[h] -= 1
                    stable_matching(hospitals, students, hospital_free_positions)
                    break
                else:
                    h_prefers_s = hospitals[h].index(s) < hospitals[h].index(students[s])
                    if not h_prefers_s:
                        continue
                    else:
                        hospital_free_positions[students[s]] += 1
                        students[s] = h
                        hospital_free_positions[h] -= 1
                        stable_matching(hospitals, students, hospital_free_positions)
                        break
    return students


hospitals = {
    'h1': ['s1', 's2', 's3'],
    'h2': ['s4', 's5', 's6']
}

students = {}
hospital_free_positions = {'h1': 2, 'h2': 3}

matching = stable_matching(hospitals, students, hospital_free_positions)

for s in matching:
    print(f"{s} is matched with {matching[s]}")
