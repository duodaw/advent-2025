import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Eleven {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("11.txt"));
        
        String line;
        HashMap<String, List<String>> map = new HashMap<>();

        while ((line = br.readLine()) != null) {
            String[] parts = line.split(": ");
            List<String> a = new ArrayList<>();
            String[] dest = parts[1].split(" ");
            for(String i: dest) {
                a.add(i);
            }
            map.put(parts[0], a);
        }
        Set<String> visited = new HashSet<>();
        System.out.println(visit(map, visited, "you"));
        br.close();
    }

    public static int visit(HashMap<String, List<String>> graph, Set<String> visited, String node) {
        if("out".equals(node)) return 1;
        visited.add(node);
        int cnt = 0;
        if(!graph.containsKey(node)) return 0;
        for(String i: graph.get(node)) {
            cnt += visit(graph, visited, i);
        }
        return cnt;
    }
}