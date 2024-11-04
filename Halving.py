def solve(N, C, R, B):
    MOD = 998244353
    
    # Check if a pair of numbers (x, y) can produce the required result based on rule
    def is_valid_pair(x, y, rule, required):
        if rule == 0:
            return min(x, y) == required
        else:
            return max(x, y) == required

    # Initialize dp array: dp[mask] represents number of valid ways for used numbers mask
    dp = {}
    used = set()  # Track numbers we've seen in C that aren't -1
    
    # Add known numbers from C to used set
    for x in C:
        if x != -1:
            used.add(x)
    
    def rec(pos):
        if pos == N:  # We've filled all positions
            return 1
            
        mask = tuple(sorted(used))  # Convert used numbers to hashable type
        state = (pos, mask)
        
        if state in dp:
            return dp[state]
            
        # Get the two positions in C we're currently looking at
        pos1 = 2 * pos
        pos2 = 2 * pos + 1
        result = 0
        
        # If both positions are known (not -1)
        if C[pos1] != -1 and C[pos2] != -1:
            # Check if these values satisfy the rule
            if is_valid_pair(C[pos1], C[pos2], R[pos], B[pos]):
                result = rec(pos + 1)
            
        # If first position is known, second unknown
        elif C[pos1] != -1:
            # Try all possible values for second position
            for val in range(1, 2*N + 1):
                if val not in used:
                    if is_valid_pair(C[pos1], val, R[pos], B[pos]):
                        used.add(val)
                        result = (result + rec(pos + 1)) % MOD
                        used.remove(val)
                        
        # If second position is known, first unknown
        elif C[pos2] != -1:
            # Try all possible values for first position
            for val in range(1, 2*N + 1):
                if val not in used:
                    if is_valid_pair(val, C[pos2], R[pos], B[pos]):
                        used.add(val)
                        result = (result + rec(pos + 1)) % MOD
                        used.remove(val)
                        
        # If both positions are unknown
        else:
            # Try all possible pairs of unused values
            for val1 in range(1, 2*N + 1):
                if val1 not in used:
                    used.add(val1)
                    for val2 in range(1, 2*N + 1):
                        if val2 not in used:
                            if is_valid_pair(val1, val2, R[pos], B[pos]):
                                used.add(val2)
                                result = (result + rec(pos + 1)) % MOD
                                used.remove(val2)
                    used.remove(val1)
        
        dp[state] = result
        return result

    return rec(0)

# Read input
N = int(input())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
B = list(map(int, input().split()))

# Print result
print(solve(N, C, R, B))