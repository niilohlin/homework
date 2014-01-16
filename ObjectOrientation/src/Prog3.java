
public class Prog3 {
	public static void main(String[] args) {
		for(int i = 0; i < args.length; i++) {
			int parsed = Integer.parseInt(args[i]);
			int result = iter_life_length(parsed);
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
	
	private static int iter_life_length(int a) {
		int counter = 0;
		while(a != 1) {
			a = f1(a);
			counter++;
		}
		return counter;
	}
}
