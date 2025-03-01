import java.io.FileWriter;
import java.io.IOException;

public class StaticAllocation {
    public static void main(String[] args) throws IOException {
        int NUM_ELEMENTS = 100000;
        long totalTime = 0;

        for (int test = 0; test < 10; test++) {
            long start = System.nanoTime();
            int[] array = new int[NUM_ELEMENTS];
            for (int i = 0; i < NUM_ELEMENTS; i++) {
                array[i] = i;
            }
            long end = System.nanoTime();
            totalTime += (end - start);
        }

        FileWriter writer = new FileWriter("./results/java_static_allocation_results.txt");
        writer.write(String.format("Average: %.6f ns\n", totalTime / 10.0));
        writer.close();
    }
}
