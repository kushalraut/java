//Program No. 11: Accept 3 numbers from user. Compare them and declare 
//the largest number (Using if-else statement)

import java.util.Scanner;
public class program11 {
    public static void main(String[] args) {
        int a ,b ,c ;
        Scanner reader = new Scanner(System.in);
        System.out.println(" Enter three integer numbers "); 
        a = reader.nextInt();
        b = reader.nextInt();
        c = reader.nextInt();
        if(a > b && a > c)
        {
            System.out.println("First No. entered is greatest "+a);

        }
        else if(b > a && b > c)
        {
            System.out.println("Second No. entered is greatest " + b);
            
        }
        else if(c > a && c > b)
        {
            System.out.println("Thrid No. entered is greatest " + c);
            
        }

        reader.close();
    }
    
}
