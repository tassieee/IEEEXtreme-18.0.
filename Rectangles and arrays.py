def get_max_area_single_pass(heights):
    n = len(heights)
    # Use arrays instead of stack for better performance
    left_smaller = [0] * n  # Index of nearest smaller element on left
    right_smaller = [0] * n  # Index of nearest smaller element on right
    
    # Find nearest smaller element on left
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left_smaller[i] = stack[-1] if stack else -1
        stack.append(i)
    
    # Find nearest smaller element on right
    stack = []
    for i in range(n-1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        right_smaller[i] = stack[-1] if stack else n
        stack.append(i)
    
    # Calculate maximum area without any modification
    max_area = 0
    for i in range(n):
        width = right_smaller[i] - left_smaller[i] - 1
        area = width * heights[i]
        max_area = max(max_area, area)
    
    return max_area, left_smaller, right_smaller

def max_rectangle_area(heights, x):
    n = len(heights)
    # Get initial maximum area and boundary arrays
    current_max, left_smaller, right_smaller = get_max_area_single_pass(heights)
    
    # For each position, we only need to try meaningful height changes
    for i in range(n):
        # Find the range this element affects
        left = left_smaller[i]
        right = right_smaller[i]
        
        # Try setting to X if it can form a larger rectangle
        if x > heights[i]:
            # Calculate potential width of rectangle
            potential_left = i
            potential_right = i
            
            # Expand left while maintaining minimum height
            j = i - 1
            while j > left and heights[j] >= x:
                potential_left = j
                j -= 1
                
            # Expand right while maintaining minimum height
            j = i + 1
            while j < right and heights[j] >= x:
                potential_right = j
                j += 1
                
            # Calculate area with this modification
            width = potential_right - potential_left + 1
            area = width * x
            current_max = max(current_max, area)
        
        # If we're not at the edges, try matching neighbors
        if i > 0 and i < n-1:
            neighbor_height = min(heights[i-1], heights[i+1])
            if neighbor_height > heights[i] and neighbor_height <= x:
                width = 0
                # Calculate width of possible rectangle with neighbor height
                j = i
                while j >= 0 and heights[j] >= neighbor_height:
                    width += 1
                    j -= 1
                j = i + 1
                while j < n and heights[j] >= neighbor_height:
                    width += 1
                    j += 1
                area = width * neighbor_height
                current_max = max(current_max, area)
    
    return current_max

def main():
    # Read input
    n, x = map(int, input().split())
    heights = list(map(int, input().split()))
    
    # Calculate and output result
    result = max_rectangle_area(heights, x)
    print(result)

if __name__ == "__main__":
    main()