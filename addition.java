import java.util.Scanner;


public class addition {

    public static void main(final String[] args) {
        
        int no1, no2, sum;
        try{
        final Scanner in1 = new Scanner(System.in);
        System.out.println("Enter First Number: ");
        no1 = in1.nextInt();
        
        System.out.println("Enter Second Number: ");
        no2 = in1.nextInt();
        
        in1.close();
        sum = no1 + no2;
        System.out.println("Sum of these numbers: "+sum);
    }
catch(final Exception e){
    System.out.println("Error is:"+e);
}
    }    
}