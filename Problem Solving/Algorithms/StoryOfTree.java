import java.util.*;

public class StoryOfTree {

List<List<Integer>> graph;
List<List<Integer>> guesses;
boolean[] visited;
int[] points;
int wins;

public int DFS_1(int vertex, int points) {
    visited[vertex] = true;
    for (int i : graph.get(vertex)) {
        if (!visited[i]) {
            if (guesses.get(vertex).contains(i)) {
                points++;
            }
            points += DFS_1(i, 0);
        }
    }
    return points;
}

public void DFS(int vertex, int k) {
    if (points[vertex] >= k) {
        wins++;
    }
    for (int i : graph.get(vertex)) {
        if (points[i] == -1) {
            if (guesses.get(vertex).contains(i) && !guesses.get(i).contains(vertex)) {
                points[i] = points[vertex] - 1;
            } else if (!guesses.get(vertex).contains(i) && guesses.get(i).contains(vertex)) {
                points[i] = points[vertex] + 1;
            } else points[i] = points[vertex];
            DFS(i, k);
        }
    }
}

public int GCD(int a, int b) {
    if (b == 0) {
        return a;
    }
    return GCD(b, a % b);
}

public void run() {
    Scanner in = new Scanner(System.in);
    int q = in.nextInt();
    while (q-- > 0) {
        int n = in.nextInt();
        graph = new ArrayList<>();
        guesses = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
            guesses.add(new ArrayList<>());
        }
        for (int i = 0; i < n - 1; i++) {
            int v1 = in.nextInt() - 1;
            int v2 = in.nextInt() - 1;
            graph.get(v1).add(v2);
            graph.get(v2).add(v1);
        }

        int g = in.nextInt();
        int k = in.nextInt();
        for (int i = 0; i < g; i++) {
            int v1 = in.nextInt() - 1;
            int v2 = in.nextInt() - 1;
            guesses.get(v1).add(v2);
        }
        visited = new boolean[n];
        points = new int[n];
        Arrays.fill(points, -1);
        points[0] = DFS_1(0, 0);

        wins = 0;
        DFS(0, k);
        int gcd = GCD(n, wins);
        System.out.println((wins / gcd) + "/" + (n / gcd));
    }
}

public static void main(String[] args) {
    new StoryOfTree().run();
}
}
