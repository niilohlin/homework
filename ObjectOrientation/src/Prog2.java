
public class Prog2 {
	public static void main(String[] args) {
		if(args.length % 2 == 0) {
			for (int i = 0; i < args.length; i += 2) {
				System.out.println(iterate_f(Integer.parseInt(args[i]),
						Integer.parseInt(args[i + 1])));
			}
		}
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
	 * @param a0 The number that should be operated on.
	 * @param n  The number of times a0 should be operated on.
	 * @return an of the Collaz function.
	 */
	private static int iterate_f(int a0, int n) {
		for(int i = 0; i <  n; i++) {
			a0 = f1(a0);
		}
		return a0;
	}
}
