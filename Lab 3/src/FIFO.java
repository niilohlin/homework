import java.util.ArrayList;
import java.util.NoSuchElementException;

/**
 * @author niil
 * Implements the Queue interface.
 */
public class FIFO implements Queue {
	/*
	 * The ArrayList is unmodified because the equality method must have access
	 * to the elements of the other FIFO.
	 */
	ArrayList<Object> array = new ArrayList<Object>();
	private int max = 0;

	
	public boolean isEmpty() {
		return array.size() == 0;
	}

	public int size() {
		return array.size();
	}


	public void add(Object e) {
		array.add(e);
		// Update the max value if size is bigger than max.
		max = size() > max ? size() : max;
	}



	public String toString() {
		String res = "Queue: ";
		for(int i = 0; i < size(); i++) {
			res += "(" + array.get(i) + ") ";
		}
		return res;

	}

	public Object first() throws NoSuchElementException {
		if(array.size() == 0) {
			throw new NoSuchElementException();
		}
		return array.get(0);
	}

	public int maxSize() {
		return max;
	}
	
	public void removeFirst() throws NoSuchElementException {
		if(array.size() == 0) {
			throw new NoSuchElementException();
		}
		array.remove(0);
	}
	
	/**
	 * Return true if the object is a FIFO and if the values of the elements in
	 * both Queues is equal.
	 */
	public boolean equals(Object obj) {
		if(!(obj instanceof FIFO)) {
			return false;
		}
		
		// Cast object to FIFO.
		FIFO other = (FIFO) obj;
		
		// Unless sizes are equal the FIFOs aren't equal.
		if(other.size() != size()) {
			return false;
		}
		
		for(int i = 0; i < size(); i++) {
			// Check for null references. Two nulls are considered equal.
			if( other.array.get(i) == null || array.get(i) == null) {
					return other.array.get(i) == null && array.get(i) == null;
			}
			
			if(!(other.array.get(i).equals(array.get(i)))) {
				return false;
			}
		}
		return true;
	}
}