def solve(N, M, constraints):
    MOD = 998244353
    
   
    def has_infinite_solutions():
       
        used_vars = set()
        for low, high, indices in constraints:
            for idx in indices:
                used_vars.add(idx)
        
        if len(used_vars) < N:
            return True
            
        for low, high, indices in constraints:
            if high == 10**18 and len(indices) >= 2:
                return True
        
        return False
    
   
    def find_max_bound():
        max_bound = 0
        for low, high, indices in constraints:
            max_bound = max(max_bound, high)
        return min(max_bound, 10**6)  
    
    def is_valid(values):
        for low, high, indices in constraints:
            sum_subset = sum(values[i-1] for i in indices)
            if sum_subset < low or sum_subset > high:
                return False
        return True
    
    if has_infinite_solutions():
        return "infinity"

    max_val = find_max_bound()
    
    def count_assignments(pos, values):
        if pos == N:
            return 1 if is_valid(values) else 0
            
        count = 0
        for val in range(max_val + 1):
            values[pos] = val
        
            valid = True
            for low, high, indices in constraints:
                if all(i-1 < pos for i in indices):  
                    sum_subset = sum(values[i-1] for i in indices)
                    if sum_subset < low or sum_subset > high:
                        valid = False
                        break
            if valid:
                count = (count + count_assignments(pos + 1, values)) % MOD
        return count
    
   
    return count_assignments(0, [0] * N)

N, M = map(int, input().split())
constraints = []
for _ in range(M):
    line = list(map(int, input().split()))
    low_i, high_i, K_i = line[0], line[1], line[2]
    indices = line[3:3+K_i]
    constraints.append((low_i, high_i, indices))

result = solve(N, M, constraints)
print(result)
