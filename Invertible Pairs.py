def get_max_subarray_sum(arr):
    max_so_far = float('-inf')
    max_ending_here = 0
    for x in arr:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def solve_test_case(n, arr):
    modified_arr = arr.copy()
    # Flip pairs where the sum is negative
    for k in range(1, (n // 2) + 1):
        pos1 = 2 * k - 2  # 0-based index
        pos2 = 2 * k - 1  # 0-based index
        if modified_arr[pos1] + modified_arr[pos2] < 0:
            modified_arr[pos1] = -modified_arr[pos1]
            modified_arr[pos2] = -modified_arr[pos2]
    # Calculate max subarray sum of the modified array
    return get_max_subarray_sum(modified_arr)

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        result = solve_test_case(N, A)
        print(result)

if __name__ == "__main__":
    main()
