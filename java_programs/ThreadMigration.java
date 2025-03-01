import java.io.FileWriter;
import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class ThreadMigration {
    private static final int NUM_ITERATIONS = 1000;

    public static void main(String[] args) throws IOException {
        long totalTime = 0;

        for (int test = 0; test < 10; test++) {
            ExecutorService executor1 = Executors.newSingleThreadExecutor();
            ExecutorService executor2 = Executors.newSingleThreadExecutor();

            long start = System.nanoTime();
            try {
                Future<?> task1 = executor1.submit(() -> {
                    for (int i = 0; i < NUM_ITERATIONS; i++);
                });
                task1.get();

                Future<?> task2 = executor2.submit(() -> {
                    for (int i = 0; i < NUM_ITERATIONS; i++);
                });
                task2.get();
            } catch (InterruptedException | java.util.concurrent.ExecutionException e) {
                e.printStackTrace();
            } finally {
                executor1.shutdown();
                executor2.shutdown();
            }
            long end = System.nanoTime();
            totalTime += (end - start);
        }

        try (FileWriter writer = new FileWriter("./results/java_thread_migration_results.txt")) {
            writer.write(String.format("Average: %.6f ns\n", totalTime / 10.0));
        }
    }
}
