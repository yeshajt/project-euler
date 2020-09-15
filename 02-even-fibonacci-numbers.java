// IMPORTANT: if downloading, change file name to EvenFibs02.java to match class name
// 02-even-fibonacci-numbers
/* By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms. */

public class EvenFibs02 {
	public static void main(String[] args) {
		int[] fibnums = new int[33]; // initialize new array such that fibval < 4m
		// append first two nums to the array
		fibnums[0] = 1;
		fibnums[1] = 1;

		int total = 0; // init total value

		for (int i = 2; i < fibnums.length; i++) {
			fibnums[i] = fibnums[i-2] + fibnums[i-1];
			if (fibnums[i] % 2 == 0) { // checks if the number is even
				total = total + fibnums[i];
			}
		}

		System.out.printf("The sum of the even-valued fibonacci numbers under 4 million is %d.\n", total);
	}
}

