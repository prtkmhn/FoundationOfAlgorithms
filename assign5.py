import sys

def optimal_ski_assignment(skis, skiers):
    m = len(skis)
    n = len(skiers)
    # Initialize c matrix with infinite values
    c = [[sys.maxsize] * (n + 1) for _ in range(m + 1)]
    # Initialize b matrix with empty values
    b = [[""] * (n + 1) for _ in range(m + 1)]
    # Set initial values of c matrix
    for i in range(m + 1):
        c[i][0] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i <= j:
                c[i][j] = min(c[i][j - 1], c[i - 1][j - 1] + abs(skis[i - 1] - skiers[j - 1]))
                if c[i][j] == c[i][j - 1]:
                    b[i][j] = "from left"
                else:
                    b[i][j] = "from diagonal"
            else:
                c[i][j] = sys.maxsize
    # Find the optimal solution
    i = m
    j = n
    assignment = [-1] * n
    while i > 0 and j > 0:
        if b[i][j] == "from diagonal":
            assignment[j - 1] = i - 1
            i -= 1
            j -= 1
        elif b[i][j] == "from left":
            j -= 1
        else:
            i -= 1
    return assignment


# Test the algorithm with sample inputs
skis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
skiers = [1, 2, 4, 5, 6, 7, 9, 10, 11, 12]
assignment = optimal_ski_assignment(skis, skiers)
print("Optimal ski assignment:")
for i in range(len(skiers)):
    print("Skier %d gets ski %d" % (i + 1, assignment[i] + 1))
