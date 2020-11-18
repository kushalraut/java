//Program No. 9: Addition of a number
import java.util.Scanner;


public class Addition {

    public static void main(String[] args) {
        
        int no1, no2, sum;
        Scanner in1 = new Scanner(System.in);
        try{
        
        System.out.println("Enter First Number: ");
        no1 = in1.nextInt();
        
        System.out.println("Enter Second Number: ");
        no2 = in1.nextInt();
        
        in1.close();
        sum = no1 + no2;
        System.out.println("Sum of these numbers: "+sum);
    }
catch(Exception e){
    System.out.println("Error is:"+e);
}
    }    
}