def solve_brick_stacks(N, x, bricks):
    # Sort bricks in descending order and keep track of original indices
    brick_pairs = [(brick, i+1) for i, brick in enumerate(bricks)]
    brick_pairs.sort(reverse=True)  # Sort by length (descending)
    
    # Initialize stacks list to store the final arrangement
    stacks = []
    used = set()
    
    # Process each brick from largest to smallest
    for brick, idx in brick_pairs:
        # If brick is already used, skip it
        if idx in used:
            continue
            
        # Start a new stack with current brick
        current_stack = [(brick, idx)]
        used.add(idx)
        last_brick = brick
        
        # Try to add more bricks to current stack
        for next_brick, next_idx in brick_pairs:
            if next_idx not in used and next_brick + x <= last_brick:
                current_stack.append((next_brick, next_idx))
                used.add(next_idx)
                last_brick = next_brick
                
        stacks.append(current_stack)
    
    return stacks

def format_output(stacks):
    # First line: number of stacks
    print(len(stacks))
    
    # For each stack: number of bricks followed by brick lengths
    for stack in stacks:
        # Print number of bricks in stack followed by their lengths
        print(len(stack), end=" ")
        # Print brick lengths from largest to smallest
        print(" ".join(str(length) for length, _ in stack))

def main():
    # Read input
    N, x = map(int, input().split())
    bricks = list(map(int, input().split()))
    
    # Solve the problem
    stacks = solve_brick_stacks(N, x, bricks)
    
    # Print output
    format_output(stacks)

if __name__ == "__main__":
    main()