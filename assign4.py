def find_closest_pair(point_list):
    def euclidean_distance(point1, point2):
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

    def closest_pair_recursive(sorted_by_x, sorted_by_y):
        n = len(sorted_by_x)
        if n <= 3:
            return min(euclidean_distance(sorted_by_x[i], sorted_by_x[j]) for i in range(n) for j in range(i + 1, n))
        mid = n // 2
        mid_x = sorted_by_x[mid][0]
        left_half = sorted_by_x[:mid]
        left_y_sorted = [p for p in sorted_by_y if p[0] <= mid_x]
        right_half = sorted_by_x[mid:]
        right_y_sorted = [p for p in sorted_by_y if p[0] > mid_x]
        z2 = closest_pair_recursive(right_half, right_y_sorted)
        z1 = closest_pair_recursive(left_half, left_y_sorted)
        z = min(z1, z2)
        s = [p for p in sorted_by_y if abs(p[0] - mid_x) <= z]
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[j][1] - s[i][1] >= z:
                    break
                z = min(z, euclidean_distance(s[i], s[j]))
        return z
    sorted_by_x = sorted(point_list, key=lambda p: p[0])
    sorted_by_y = sorted(point_list, key=lambda p: p[1])
    return closest_pair_recursive(sorted_by_x, sorted_by_y)

# Test case with 16 points
points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20), (21, 22), (23, 24), (25, 26), (27, 28), (29, 30), (31, 32)]
print(find_closest_pair(points))
