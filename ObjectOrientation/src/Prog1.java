
public class Prog1 {
	public static void main(String[] args) {
		// Parse all the args. Assume they are ints.
		for(int i = 0; i < args.length; i++) {
			System.out.println(f1(Integer.parseInt(args[i])));
		}
		
		for(int i = 0; i < args.length; i++) {
			System.out.println("f1 = " + f1(Integer.parseInt(args[i])) + 
							   " f2 = " + f2(Integer.parseInt(args[i])) +
							   " f4 = " + f4(Integer.parseInt(args[i])) +
							   " f8 = " + f8(Integer.parseInt(args[i])) +
							   " f16 = " + f16(Integer.parseInt(args[i])) +
							   " f32 = " + f32(Integer.parseInt(args[i])) +
							   " f64 = " + f64(Integer.parseInt(args[i])));
		}
	}
	
	
	/**
	 * @param n Any positive integer n.
	 * @return Collaz function of that number.
	 */
	private static int f1(int n) {
		if (n == 1) {
			return 1;
		} else if (n % 2 == 0) {
			return n / 2;
		}
		return 3 * n + 1;
	}
	
	private static int f2(int n) {
		return f1(f1(n));
	}
	
	private static int f4(int n) {
		return f2(f2(n));
	}
	private static int f8(int n) {
		return f4(f4(n));
	}
	private static int f16(int n) {
		return f8(f8(n));
	}
	private static int f32(int n) {
		return f16(f16(n));
	}
	private static int f64(int n) {
		return f32(f32(n));
	}
}
