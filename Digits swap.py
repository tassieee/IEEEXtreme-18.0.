def get_max_after_swaps(N, K):
    digits = list(str(N))
    n = len(digits)
    k = K
    
    # For each position from left to right
    i = 0
    while i < n and k > 0:
        # Find max digit's index from i to end
        max_idx = i
        for j in range(i + 1, n):
            if digits[j] > digits[max_idx]:
                max_idx = j
        
        # If current position doesn't have max digit
        if max_idx != i:
            # Find rightmost occurrence of max digit
            max_digit = digits[max_idx]
            for j in range(n-1, i-1, -1):
                if digits[j] == max_digit:
                    max_idx = j
                    break
            
            # Swap max digit to current position
            digits[max_idx], digits[i] = digits[i], digits[max_idx]
            k -= 1
        i += 1
    
    # If we have remaining swaps, try to optimize last two digits
    if k > 0:
        # Check if swapping last two digits gives larger number
        for i in range(n-1):
            for j in range(i+1, n):
                # Try swap and compare
                digits[i], digits[j] = digits[j], digits[i]
                new_num = ''.join(digits)
                original = ''.join(digits)
                digits[i], digits[j] = digits[j], digits[i]  # swap back
                
                if new_num > original:
                    digits[i], digits[j] = digits[j], digits[i]
                    k -= 1
                    if k == 0:
                        break
            if k == 0:
                break
                
    return int(''.join(digits))

def main():
    N, K = map(int, input().split())
    print(get_max_after_swaps(N, K))

if __name__ == "__main__":
    main()