from bisect import bisect_right


L, N, M = map(int, input().split())

upper_A, upper_B = set(), set()
count_right_A = 0
count_left_B = 0


for _ in range(N):
    direction, coordinate = input().split()
    coordinate = int(coordinate)
    if direction == 'U':
        upper_A.add(coordinate)
    elif direction == 'R':
        count_right_A += 1


for _ in range(M):
    direction, coordinate = input().split()
    coordinate = int(coordinate)
    if direction == 'U':
        upper_B.add(coordinate)
    elif direction == 'L':
        count_left_B += 1


upper_A = sorted(upper_A)
upper_B = sorted(upper_B)


lines_by_A = len(upper_A) + count_right_A
total_areas = (lines_by_A + 1) * (count_left_B + 1)


for beam in upper_B:
    # Use binary search to count beams in upper_A that are smaller or equal to the current beam
    total_areas += lines_by_A + 1 - bisect_right(upper_A, beam)


print(total_areas)
