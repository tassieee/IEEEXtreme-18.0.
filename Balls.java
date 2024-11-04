import java.util.Scanner;

class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long N = scanner.nextLong();
        int K = scanner.nextInt();
        int[] elasticities = new int[K];

        for (int i = 0; i < K; i++) {
            elasticities[i] = scanner.nextInt();
        }

        long result = countHitTiles(N, K, elasticities);
        System.out.println(result);
    }

    private static long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    private static long lcm(long a, long b) {
        return (a / gcd(a, b)) * b;
    }

    private static long countHitTiles(long N, int K, int[] elasticities) {
        long uniqueCount = 0;

        for (int i = 1; i < (1 << K); i++) {
            long lcm = 1;
            int bits = 0;

            for (int j = 0; j < K; j++) {
                if ((i & (1 << j)) != 0) {
                    bits++;
                    lcm = lcm(lcm, elasticities[j]);
                    if (lcm > N) {
                        break; // Early exit if LCM exceeds N
                    }
                }
            }

            // Apply the inclusion-exclusion principle
            if (lcm <= N) {
                // Use the parity of bits to determine addition or subtraction
                uniqueCount += (bits % 2 == 1 ? 1 : -1) * (N / lcm);
            }
        }

        return uniqueCount;
    }
}
