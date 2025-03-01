import java.io.FileWriter;
import java.io.IOException;

public class ThreadContextSwitch {
    private static final int NUM_ITERATIONS = 1000;

    public static void main(String[] args) throws IOException {
        long totalTime = 0;
        for (int test = 0; test < 10; test++) 
        {
            Thread worker1 = new Thread(() -> 
            {
                for (int i = 0; i < NUM_ITERATIONS; i++);
            });
            Thread worker2 = new Thread(() -> 
            {
                for (int i = 0; i < NUM_ITERATIONS; i++);
            });
            long start = System.nanoTime();
            worker1.start();
            worker2.start();
            try 
            {
                worker1.join();
                worker2.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            long end = System.nanoTime();
            totalTime += (end - start);
        }

        try (FileWriter writer = new FileWriter("./results/java_thread_context_switch_results.txt")) {
            writer.write(String.format("Average: %.6f ns\n", totalTime / 10.0));
        }
    }
}
