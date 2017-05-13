/*
	Vinicius Sesti <vinicius.s.sesti@gmail.com>
	Project Euler: Problem 4

	A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
	Find the largest palindrome made from the product of two 3-digit numbers.
*/

public class Problem4
{
	public static void main(String[] args)
	{
		int largest = 0;

		for (int n1=999;n1>0;n1--)
			for(int n2=999;n2>0;n2--)
				if(n2*n1>largest && new StringBuilder(""+n2*n1).reverse().toString().equals(""+n2*n1))
					largest = n2*n1;
		System.out.println(largest); 
	}
}