def solve(N, M, constraints):
    MOD = 998244353
    
    # Check for infinite solutions
    def has_infinite_solutions():
        # If any variable is unconstrained and non-negative,
        # it can take infinitely many values
        used_vars = set()
        for low, high, indices in constraints:
            for idx in indices:
                used_vars.add(idx)
        
        # If any variable is unused and can be any non-negative number,
        # we have infinite solutions
        if len(used_vars) < N:
            return True
            
        # If any high bound is 10^18, variables in that constraint
        # might be able to grow infinitely while maintaining sum constraint
        for low, high, indices in constraints:
            if high == 10**18 and len(indices) >= 2:
                return True
        
        return False
    
    # Find maximum possible value for any variable
    def find_max_bound():
        max_bound = 0
        for low, high, indices in constraints:
            max_bound = max(max_bound, high)
        return min(max_bound, 10**6)  # Use reasonable bound for computation
    
    # Check if assignment satisfies all constraints
    def is_valid(values):
        for low, high, indices in constraints:
            sum_subset = sum(values[i-1] for i in indices)
            if sum_subset < low or sum_subset > high:
                return False
        return True
    
    # If infinite solutions exist, return early
    if has_infinite_solutions():
        return "infinity"
    
    # Find maximum bound for variables
    max_val = find_max_bound()
    
    # Recursive function to try all possible assignments
    def count_assignments(pos, values):
        if pos == N:
            return 1 if is_valid(values) else 0
            
        count = 0
        for val in range(max_val + 1):
            values[pos] = val
            # Early pruning: check if partial assignment already violates constraints
            valid = True
            for low, high, indices in constraints:
                if all(i-1 < pos for i in indices):  # if all variables in constraint are set
                    sum_subset = sum(values[i-1] for i in indices)
                    if sum_subset < low or sum_subset > high:
                        valid = False
                        break
            if valid:
                count = (count + count_assignments(pos + 1, values)) % MOD
        return count
    
    # Start counting from first position
    return count_assignments(0, [0] * N)

# Example usage:
N, M = map(int, input().split())
constraints = []
for _ in range(M):
    line = list(map(int, input().split()))
    low_i, high_i, K_i = line[0], line[1], line[2]
    indices = line[3:3+K_i]
    constraints.append((low_i, high_i, indices))

result = solve(N, M, constraints)
print(result)