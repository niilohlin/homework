
public class Prog4 {
	public static void main(String[] args) {
		
	}
	
	/**
	 * Raises x to the k'th power.
	 * @param x. The base.
	 * @param k. The power
	 * @return x^{k}.
	 */
	private static double rec_raise_eff(double x, int k) {
		if(k == 0) {
			return 1;
		} else if (k % 2 == 0) {
			/* 
			 * Make a new variable because 
			 * rec_raise_eff(x, k / 2) * rec_raise_eff(x, k / 2);
			 * would calculate the function twice. 
			 */
			double res = rec_raise_eff(x, k / 2);
			return res * res;
		} else {
			double res = rec_raise_eff(x, k / 2);
			return x * res * res;
		}
	}

}
