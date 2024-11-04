from math import gcd
from typing import List, Tuple

class SalaryHappinessTracker:
    def __init__(self, n: int, initial_salaries: List[int]):
        self.n = n
        # Initialize salaries and happiness arrays
        self.salaries = initial_salaries.copy()
        self.happiness = [0] * n  # Initial happiness is 0 for all employees
        
    def reduce_fraction(self, p: int, q: int) -> Tuple[int, int]:
        """Reduces fraction p/q to its lowest terms."""
        if q == 0:
            return (0, 1)
        d = gcd(abs(p), abs(q))
        return (p // d, q // d)
    
    def process_event_0(self, l: int, r: int, c: int):
        """Set salary to c for employees from l to r."""
        for i in range(l-1, r):
            old_salary = self.salaries[i]
            self.salaries[i] = c
            # Update happiness based on salary change
            if c > old_salary:
                self.happiness[i] += 1
            elif c < old_salary:
                self.happiness[i] -= 1
    
    def process_event_1(self, l: int, r: int, c: int):
        """Change salary by c for employees from l to r."""
        for i in range(l-1, r):
            old_salary = self.salaries[i]
            self.salaries[i] += c
            # Update happiness based on salary change
            if c > 0:
                self.happiness[i] += 1
            elif c < 0:
                self.happiness[i] -= 1
    
    def query_salary_average(self, l: int, r: int) -> Tuple[int, int]:
        """Calculate average salary for employees from l to r."""
        total = sum(self.salaries[l-1:r])
        count = r - l + 1
        return self.reduce_fraction(total, count)
    
    def query_happiness_average(self, l: int, r: int) -> Tuple[int, int]:
        """Calculate average happiness for employees from l to r."""
        total = sum(self.happiness[l-1:r])
        count = r - l + 1
        return self.reduce_fraction(total, count)

def main():
    # Read input
    N, Q = map(int, input().split())
    initial_salaries = list(map(int, input().split()))
    
    # Initialize tracker
    tracker = SalaryHappinessTracker(N, initial_salaries)
    
    # Process queries
    for _ in range(Q):
        query = list(map(int, input().split()))
        query_type = query[0]
        
        if query_type == 0:
            # Set salary event
            _, l, r, c = query
            tracker.process_event_0(l, r, c)
        
        elif query_type == 1:
            # Change salary event
            _, l, r, c = query
            tracker.process_event_1(l, r, c)
        
        elif query_type == 2:
            # Query average salary
            _, l, r = query
            p, q = tracker.query_salary_average(l, r)
            print(f"{p}/{q}")
        
        elif query_type == 3:
            # Query average happiness
            _, l, r = query
            p, q = tracker.query_happiness_average(l, r)
            print(f"{p}/{q}")

if __name__ == "__main__":
    main()