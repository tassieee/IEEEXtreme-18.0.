def get_optimal_cost(arr):
    """
    Calculate the optimal cost for a sorted array by finding the minimum possible matching cost.
    For sorted array, optimal pairing strategy is to pair smallest with largest elements.
    """
    n = len(arr)
    if n == 1:
        return arr[0]
        
    if n == 2:
        return arr[0] + arr[1]
    
    # For even length
    if n % 2 == 0:
        pairs = []
        for i in range(n//2):
            pairs.append(arr[i] + arr[n-1-i])
        return max(pairs)
    else:
        # For odd length, middle element as single is optimal for sorted array
        mid = n//2
        pairs = []
        for i in range(mid):
            pairs.append(arr[i] + arr[n-1-i])
        return max(pairs + [arr[mid]])

def solve_queries(N, Q, A, queries):
    """
    Optimize query processing using binary search and efficient optimal cost calculation
    """
    results = []
    for x in queries:
        total = 0
        # For each possible subarray
        for left in range(N):
            for right in range(left, N):
                # Calculate optimal cost directly for current subarray
                opt_cost = get_optimal_cost(A[left:right+1])
                if opt_cost <= x:
                    total += A[right] - A[left]
        results.append(total)
    
    return results

def main():
    # Read input
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    queries = [int(input()) for _ in range(Q)]
    
    # Solve queries
    results = solve_queries(N, Q, A, queries)
    
    # Output results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()