class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.n = 1
        while self.n < size:
            self.n *= 2
        self.tree = [0] * (2 * self.n)
        self.lazy = [0] * (2 * self.n)
    
    def propagate(self, x, lx, rx):
        if self.lazy[x] == 0:
            return
        self.tree[x] += self.lazy[x] * (rx - lx)
        if rx - lx > 1:
            self.lazy[2*x+1] += self.lazy[x]
            self.lazy[2*x+2] += self.lazy[x]
        self.lazy[x] = 0
    
    def update_range(self, l, r, v, x, lx, rx):
        self.propagate(x, lx, rx)
        if lx >= r or rx <= l:
            return
        if lx >= l and rx <= r:
            self.lazy[x] += v
            self.propagate(x, lx, rx)
            return
        mid = (lx + rx) // 2
        self.update_range(l, r, v, 2*x+1, lx, mid)
        self.update_range(l, r, v, 2*x+2, mid, rx)
        self.tree[x] = self.tree[2*x+1] + self.tree[2*x+2]
    
    def query_range(self, l, r, x, lx, rx):
        self.propagate(x, lx, rx)
        if lx >= r or rx <= l:
            return 0
        if lx >= l and rx <= r:
            return self.tree[x]
        mid = (lx + rx) // 2
        return (self.query_range(l, r, 2*x+1, lx, mid) + 
                self.query_range(l, r, 2*x+2, mid, rx))
    
    def update(self, l, r, v):
        self.update_range(l-1, r, v, 0, 0, self.n)
    
    def query(self, l, r):
        return self.query_range(l-1, r, 0, 0, self.n)

def solve():
    # Read input
    N, Q = map(int, input().split())
    P = list(map(int, input().split()))
    
    # Create and initialize trees for different purposes:
    # 1. direct_tree: for type 0 updates viewed normally
    # 2. perm_tree: for type 1 updates viewed normally
    # 3. perm_to_direct: for type 1 updates viewed through inverse permutation
    # 4. direct_to_perm: for type 0 updates viewed through permutation
    direct_tree = SegmentTree(N)
    perm_tree = SegmentTree(N)
    perm_to_direct = SegmentTree(N)
    direct_to_perm = SegmentTree(N)
    
    # Precompute permutation mappings
    P_idx = [0] * (N + 1)  # P[i] -> i+1 mapping
    for i in range(N):
        P_idx[P[i]] = i + 1
    
    results = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        t = query[0]
        
        if t <= 1:  # Updates
            l, r, c = query[1:]
            if t == 0:  # Direct update
                direct_tree.update(l, r, c)
                # Update the permuted view of direct updates
                for i in range(l, r + 1):
                    if i <= N:
                        perm_pos = P_idx[i]
                        if perm_pos:
                            direct_to_perm.update(perm_pos, perm_pos, c)
            else:  # Update through permutation
                perm_tree.update(l, r, c)
                # Update the direct view of permuted updates
                for i in range(l, r + 1):
                    if i <= N:
                        actual_pos = P[i - 1]
                        perm_to_direct.update(actual_pos, actual_pos, c)
        else:  # Queries
            l, r = query[1:]
            if t == 2:  # Direct query
                # Sum of direct updates and permuted updates viewed directly
                result = direct_tree.query(l, r) + perm_to_direct.query(l, r)
                results.append(result)
            else:  # Query through permutation
                # Sum of permuted updates and direct updates viewed through permutation
                result = perm_tree.query(l, r) + direct_to_perm.query(l, r)
                results.append(result)
    
    # Print results
    for result in results:
        print(result)

# Run the solution
solve()