
public class Prog3 {
	public static void main(String[] args) {
		for(int i = 0; i < args.length; i++) {
			int parsed = Integer.parseInt(args[i]);
			int result = iter_life_length(parsed);
			System.out.println(format(parsed, result));
			result = rec_life_length(parsed);
			System.out.println(format(parsed, result));
		}
	}
	
	/**
	 * Return a formated string suitable for printing.
	 */
	private static String format(int x, int y) {
		return "The life length of " + x + " is " + y;
	}

	private static int f1(int n) {
		if (n == 1) {
			return 1;
		} else if (n % 2 == 0) {
			return n / 2;
		}
		return 3 * n + 1;
	}
	
	/**
	 * @param a
	 * @return The number of iterations of the Collaz function before a reaches
	 * one
	 */
	private static int iter_life_length(int a) {
		int counter = 0;
		while(a != 1) {
			a = f1(a);
			counter++;
		}
		return counter;
	}
	
	/**
	 * Same as above. But slower and using more memory.
	 */
	private static int rec_life_length(int a) {
		return (a == 1) ? 0 : 1 + rec_life_length(f1(a));
	}
}
