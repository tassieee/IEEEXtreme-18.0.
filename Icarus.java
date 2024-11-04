import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String S = in.next(); // Read the movement string

        int N = Math.min(2 * S.length(), 1000); // Define maximum N based on constraints
        int A = 1; // Starting node
        int B = N; // Set exit node to the last node

        // Check if a valid configuration can be made
        if (B <= 0 || B > N || A == B) {
            System.out.println(-1); // Exit node must not be the same as start node
            return;
        }

        // Create the binary tree representation
        int[][] tree = new int[N + 1][2]; // Array for left and right children

        for (int i = 1; i <= N; i++) {
            // Assign children in a way to avoid exit B
            if (2 * i <= N) {
                tree[i][0] = 2 * i; // Left child
            } else {
                tree[i][0] = 0; // No left child
            }

            if (2 * i + 1 <= N) {
                tree[i][1] = 2 * i + 1; // Right child
            } else {
                tree[i][1] = 0; // No right child
            }
        }

        // Override the exit node so that it has no valid children
        if (B <= N) {
            tree[B][0] = 0; // Ensure exit has no left child
            tree[B][1] = 0; // Ensure exit has no right child
        }

        // Output the results
        System.out.println(N + " " + A + " " + B);
        for (int i = 1; i <= N; i++) {
            System.out.println(tree[i][0] + " " + tree[i][1]); // Print children
        }
    }
}
