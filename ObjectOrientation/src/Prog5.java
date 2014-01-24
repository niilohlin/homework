
public class Prog5 {
	private static int counter;
	public static void main(String[] args) {
		test_small();
	}

	private static double rec_raise_eff(double x, int k) {
		counter++;
		if(k == 0) {
			return 1;
		} else if (k % 2 == 0) {
			double res = rec_raise_eff(x, k / 2);
			return res * res;
		} else {
			double res = rec_raise_eff(x, k / 2);
			return x * res * res;
		}
	}
	
	private static double rec_raise(double x, int k) {
		counter++;
		if (k == 0) {
			return 1;
		} else {
			return x * rec_raise(x, k-1);
		}
	}
	
	private static int testrre(double x, int k) {
		counter = 0;
		rec_raise_eff(x, k);
		System.out.println("rec_raise_eff: " + counter + " times");
		return counter;
	}

	private static int testrr(double x, int k) {
		counter = 0;
		rec_raise(x, k);
		return counter;
	}
	
	private static void test_small() {
		double x = 1.0001;
		// TODO Make lists and feed the to gnuplot.
		int sampleSize = 50;
		int[] testrrData = new int[sampleSize];
		int[] testrreData = new int[sampleSize];
		for(int k = 1; k <= sampleSize; k++) {
			testrrData[k-1] = testrr(x, k);
			testrreData[k-1] = testrre(x, k);
		}
		for(int i : testrrData)
			
			System.out.println(i);
		for(int i : testrreData)
			System.out.println(i);
	}
}
