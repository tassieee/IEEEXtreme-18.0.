import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the number of projects and dependencies
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        
        // Read the group IDs for each project
        int[] groupIds = new int[N];
        for (int i = 0; i < N; i++) {
            groupIds[i] = scanner.nextInt();
        }
        
        // Read the dependencies
        List<int[]> dependencies = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            int A = scanner.nextInt();
            int B = scanner.nextInt();
            dependencies.add(new int[]{A, B});
        }
        
        // Get the project order
        List<Integer> result = findProjectOrder(N, M, groupIds, dependencies);
        
        // Output the result
        if (result == null) {
            System.out.println(-1);
        } else {
            for (int project : result) {
                System.out.print(project + " ");
            }
            System.out.println();
        }
        
        scanner.close();
    }

    private static List<Integer> findProjectOrder(int N, int M, int[] groupIds, List<int[]> dependencies) {
        // Graph initialization
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        
        int[] inDegree = new int[N + 1];
        
        // Build the graph from dependencies
        for (int[] dep : dependencies) {
            int A = dep[0];
            int B = dep[1];
            graph.get(A).add(B);
            inDegree[B]++;
        }
        
        // Priority queue to manage the order based on (group_id, project_id)
        PriorityQueue<Project> priorityQueue = new PriorityQueue<>(
            (a, b) -> a.groupId != b.groupId ? Integer.compare(a.groupId, b.groupId) : Integer.compare(a.projectId, b.projectId)
        );

        // Initialize the queue with projects that have no dependencies (in_degree == 0)
        for (int project = 1; project <= N; project++) {
            if (inDegree[project] == 0) {
                priorityQueue.offer(new Project(groupIds[project - 1], project));
            }
        }
        
        List<Integer> sortedOrder = new ArrayList<>();
        
        while (!priorityQueue.isEmpty()) {
            // Pick the project with the smallest group ID (and project ID if tie)
            Project current = priorityQueue.poll();
            sortedOrder.add(current.projectId);
            
            // Process the neighbors of the current project
            for (int neighbor : graph.get(current.projectId)) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    priorityQueue.offer(new Project(groupIds[neighbor - 1], neighbor));
                }
            }
        }
        
        // If we processed all projects, return the order; else, there's a cycle
        return sortedOrder.size() == N ? sortedOrder : null;
    }
    
    // Helper class to hold project information
    static class Project {
        int groupId;
        int projectId;
        
        Project(int groupId, int projectId) {
            this.groupId = groupId;
            this.projectId = projectId;
        }
    }
}
