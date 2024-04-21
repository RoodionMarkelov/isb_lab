/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.Random;

public class Main
{
	 public static void main(String args[])
    {
        StringBuilder sequence = new StringBuilder();
        
        Random rand = new Random();
        
        for (int i = 0; i < 128; i++) {
            int rand_bit = rand.nextInt(2);
            sequence.append(rand_bit);
        }
        
        System.out.println("Random Sequence: " + sequence);
    }
}
