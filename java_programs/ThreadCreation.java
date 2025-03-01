import java.io.FileWriter;
import java.io.IOException;

public class ThreadCreation {
    public static void main(String[] args) throws IOException {
        int NUM_THREADS = 1000;
        long totalTime = 0;

        for (int test = 0; test < 10; test++) {
            long start = System.nanoTime();
            Thread[] threads = new Thread[NUM_THREADS];
            for (int i = 0; i < NUM_THREADS; i++) {
                threads[i] = new Thread(() -> {});
                threads[i].start();
            }
            for (int i = 0; i < NUM_THREADS; i++) {
                try {
                    threads[i].join();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            long end = System.nanoTime();
            totalTime += (end - start);
        }

        FileWriter writer = new FileWriter("./results/java_thread_creation_results.txt");
        writer.write(String.format("Average: %.6f ns\n", totalTime / 10.0));
        writer.close();
    }
}
