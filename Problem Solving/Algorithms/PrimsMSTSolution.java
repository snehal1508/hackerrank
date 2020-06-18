import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Pair implements Comparable<Pair>{
    int nei;
    int wei;

    public Pair(int nei, int wei) {
        this.nei = nei;
        this.wei = wei;
    }

    public int compareTo(Pair b) {
        if (wei<b.wei) return -1;
        else if (wei == b.wei) return 0;
        else return 1;
    }
}

public class Solution {

    // Complete the prims function below.
    static int prims(int n, int[][] edges, int start) {
        boolean[] visited = new boolean[n];
        PriorityQueue<Pair> pq = new PriorityQueue<>();
        List<List<Pair>> adj = new ArrayList<>();
        for (int i = 0; i<n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i<edges.length; i++) {
            int f = edges[i][0]-1;
            int t = edges[i][1]-1;
            int w = edges[i][2];
            adj.get(f).add(new Pair(t, w));
            adj.get(t).add(new Pair(f, w));
        }
        pq.offer(new Pair(start-1, 0));
        int res = 0;
        while (!pq.isEmpty()) {
            Pair cur = pq.poll();
            if (!visited[cur.nei]) {
                List<Pair> neighbors = adj.get(cur.nei);
                for (int i = 0; i<neighbors.size(); i++) {
                    Pair tmp = neighbors.get(i);
                    if (!visited[tmp.nei]) pq.offer(tmp);
                }
                visited[cur.nei] = true;
                res += cur.wei;
            }
        }
        return res;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nm = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nm[0]);

        int m = Integer.parseInt(nm[1]);

        int[][] edges = new int[m][3];

        for (int i = 0; i < m; i++) {
            String[] edgesRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 3; j++) {
                int edgesItem = Integer.parseInt(edgesRowItems[j]);
                edges[i][j] = edgesItem;
            }
        }

        int start = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int result = prims(n, edges, start);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
