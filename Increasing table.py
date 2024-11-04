import sys
import threading

def main():
    import sys

    sys.setrecursionlimit(1 << 25)
    MOD = 998244353

    N_and_rest = sys.stdin.read().split()
    N = int(N_and_rest[0])
    idx = 1
    X = int(N_and_rest[idx])
    idx += 1
    A = set()
    for _ in range(X):
        A.add(int(N_and_rest[idx]))
        idx +=1
    Y = int(N_and_rest[idx])
    idx += 1
    B = set()
    for _ in range(Y):
        B.add(int(N_and_rest[idx]))
        idx +=1

    positions = [i+1 for i in range(2*N)]

    fixed = [0] * (2*N + 1)  # 1-based indexing
    for i in range(1, 2*N + 1):
        num = positions[i - 1]
        if num in A:
            fixed[i] = 1  # Must be up step
        elif num in B:
            fixed[i] = -1  # Must be down step
        else:
            fixed[i] = 0  # Can be up or down

    dp = [[0]*(N+1) for _ in range(2*N+1)]
    dp[0][0] = 1

    for i in range(0, 2*N):
        for h in range(N+1):
            if dp[i][h]:
                val = dp[i][h]
                if fixed[i+1] == 1:
                    if h + 1 <= N:
                        dp[i+1][h+1] = (dp[i+1][h+1] + val)%MOD
                elif fixed[i+1] == -1:
                    if h > 0:
                        dp[i+1][h-1] = (dp[i+1][h-1] + val)%MOD
                else:
                    if h + 1 <= N:
                        dp[i+1][h+1] = (dp[i+1][h+1] + val)%MOD
                    if h > 0:
                        dp[i+1][h-1] = (dp[i+1][h-1] + val)%MOD

    answer = dp[2*N][0] % MOD
    print(answer)

threading.Thread(target=main).start()