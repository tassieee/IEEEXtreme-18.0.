import java.math.BigInteger;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine(); // Read the input as a string
        BigInteger N = new BigInteger(input); // Use BigInteger to handle large numbers

        // Check if N is 0 or 1 as special cases
        if (N.equals(BigInteger.ZERO)) {
            System.out.println(-1); // 3^x cannot be 0
            return;
        } else if (N.equals(BigInteger.ONE)) {
            System.out.println(0); // 3^0 = 1
            return;
        }

        BigInteger power = BigInteger.ONE; // This will hold 3^x
        int x = 0; // Exponent
        
        while (power.compareTo(N) < 0) {
            power = power.multiply(BigInteger.valueOf(3)); // Increase power by multiplying by 3
            x++; // Increment exponent
        }

        // After exiting the loop, check if we found a match
        if (power.equals(N)) {
            System.out.println(x); // Print x if we found it
        } else {
            System.out.println(-1); // Print -1 if N is not a power of 3
        }
    }
}
