N = int(input())
substances = [tuple(map(int, input().split())) for _ in range(N)]

found = False
min_T1 = None
min_T2 = None

for T1 in range(-100, 101):
    for T2 in range(T1, 101):
        possible = True
        for ai, bi in substances:
            if T1 < ai or T1 > bi:
                if T2 < ai or T2 > bi:
                    possible = False
                    break
        if possible:
            if not found or T1 < min_T1 or (T1 == min_T1 and T2 < min_T2):
                min_T1 = T1
                min_T2 = T2
                found = True
    if found and min_T1 == -100:
        break

if found:
    print(f"{min_T1} {min_T2}")
else:
    print(-1)
