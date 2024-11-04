import sys

def normalize_coordinate(x, min_x, max_x):
    if max_x == min_x:
        return 0
    else:
        return int((x - min_x) * 65535 / (max_x - min_x))

def interleave_bits16(x, y):
    x &= 0xFFFF
    y &= 0xFFFF
    x = (x | (x << 8)) & 0x00FF00FF
    x = (x | (x << 4)) & 0x0F0F0F0F
    x = (x | (x << 2)) & 0x33333333
    x = (x | (x << 1)) & 0x55555555

    y = (y | (y << 8)) & 0x00FF00FF
    y = (y | (y << 4)) & 0x0F0F0F0F
    y = (y | (y << 2)) & 0x33333333
    y = (y | (y << 1)) & 0x55555555

    return x | (y << 1)

def main():
    input_lines = sys.stdin.read().splitlines()
    N = int(input_lines[0].strip())
    points = [tuple(map(int, line.strip().split())) for line in input_lines[1:]]

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    x_norm = [normalize_coordinate(x, min_x, max_x) for x in xs]
    y_norm = [normalize_coordinate(y, min_y, max_y) for y in ys]

    morton_codes = [interleave_bits16(x_norm[i], y_norm[i]) for i in range(N)]

    sorted_indices = sorted(range(N), key=lambda i: morton_codes[i])

    groups = []
    for i in range(0, N, 3):
        group = sorted_indices[i:i+3]
        if len(group) == 3:
            groups.append(group)
    
    for group in groups:
        print(" ".join(map(str, group)))

if __name__ == "__main__":
    main()
