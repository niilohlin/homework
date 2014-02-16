import java.io.File;
import java.io.IOException;
import java.util.Scanner;

/**
 * Implement the readFile function.
 */
public class GraphIO {
	
	/**
	 * Read a well formated file into a graph.
	 * @param g
	 *            the graph in which to load the nodes and edges.
	 * @param filename
	 *            the path.
	 * @throws IOException
	 *             on bad pathname.
	 */
	public static void readFile(Graph g, String filename) throws IOException {
		Scanner s = new Scanner(new File(filename));
		int n = s.nextInt();
		
		for (int i = 0; i < n; i++) {
			// Try to read everything. If poorly formated or not ints. Fail.
			g.addNode(s.nextInt(), s.nextInt(), s.nextInt());
		}

		while (s.hasNextInt()) {
			// Connect the nodes.
			g.addEdge(s.nextInt(), s.nextInt(), s.nextInt());	
		}
	}

}
