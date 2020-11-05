//5 display multiplication table of 15 using while loop 
import java.util.Scanner;
public class prac6 {
    public static void main(String[] args) {
        int i=1;
        Scanner read = new Scanner(System.in);
        System.out.println("Enter range ");
        int n = read.nextInt();
        System.out.println("--15 Multiplication table--");
        while(i<=n)
        {
            
            System.out.println(15+" X "+i+" = "+15*i);
            i=i+1;
            
        }
        read.close();
    }
    
}
