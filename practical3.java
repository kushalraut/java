// 3 accept three numbers from user.compare them and declare the largest number (using if-self statement)
import java.util.Scanner;
public class prac4 {
    public static void main(String[] args) {
        int a ,b ,c ;
        Scanner reader = new Scanner(System.in);
        System.out.println(" Enter three integer numbers "); 
        a = reader.nextInt();
        b = reader.nextInt();
        c = reader.nextInt();
        if(a > b && a > c)
        {
            System.out.println("a is greatest "+a);

        }
        else if(b > a && b > c)
        {
            System.out.println("b is greatest " + b);
            
        }
        else if(c > a && c > b)
        {
            System.out.println("c is greatest " + c);
            
        }

        reader.close();
    }
    
}
