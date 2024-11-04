def compute_area(N, K, L):
    area_one_square = 4 * L * L
    overlap = max(0, 2 * L - K)
    overlap_area = overlap * overlap
    total_area = N * area_one_square - (N - 1) * overlap_area
    return total_area

N, K, L = map(int, input().split())

print(compute_area(N, K, L))