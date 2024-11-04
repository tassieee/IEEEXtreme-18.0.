from collections import defaultdict
import sys
sys.setrecursionlimit(10**5 + 10)  # Safely handle larger inputs

def find_max_restaurants(n, stars, roads):
    # Create adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v in roads:
        graph[u-1].append(v-1)  # Convert to 0-based indexing
        graph[v-1].append(u-1)
    
    # Cache for memoization: (current, last_stars, visited_hash)
    dp = {}
    
    def dfs(current, parent, last_stars, path_mask):
        # Memoization check
        state = (current, last_stars, path_mask)
        if state in dp:
            return dp[state]
        
        max_restaurants = 0
        current_mask = path_mask | (1 << current)
        
        # Explore each neighbor
        for neighbor in graph[current]:
            if neighbor != parent and not (path_mask & (1 << neighbor)):
                # If eating here, only continue if stars[current] > last_stars
                if stars[current] > last_stars:
                    eat_path = 1 + dfs(neighbor, current, stars[current], current_mask)
                    max_restaurants = max(max_restaurants, eat_path)
                
                # Skip eating at the current restaurant
                skip_path = dfs(neighbor, current, last_stars, current_mask)
                max_restaurants = max(max_restaurants, skip_path)
        
        # Handle leaf nodes
        if stars[current] > last_stars and all(path_mask & (1 << neigh) for neigh in graph[current] if neigh != parent):
            max_restaurants = max(max_restaurants, 1)
        
        # Save result to avoid recomputation
        dp[state] = max_restaurants
        return max_restaurants

    global_max = 0
    
    # Find leaves (nodes with only one connection)
    leaves = [i for i in range(n) if len(graph[i]) == 1]
    
    # Define high-value nodes
    high_value_nodes = set(i for i in range(n) if stars[i] > min(stars))
    start_nodes = set(leaves) | high_value_nodes
    
    # Traverse each start node
    for start in start_nodes:
        result_if_eat = 1 + dfs(start, -1, stars[start], 0)
        result_if_skip = dfs(start, -1, -1, 0)
        global_max = max(global_max, result_if_eat, result_if_skip)
    
    return global_max

def main():
    try:
        input = sys.stdin.read
        data = input().splitlines()
        n = int(data[0])
        stars = list(map(int, data[1].split()))
        roads = [tuple(map(int, line.split())) for line in data[2:]]
        
        global_max = find_max_restaurants(n, stars, roads)
        print(global_max)
        return 0
        
    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
