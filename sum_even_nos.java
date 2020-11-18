//Program No.11: Display sum of first 10 even nos.using do-while loop. 
public class sum_even_nos {
    public static void main(String[] args) {
        int x=0,sum=0,count=0;
       do{
           sum=sum+x;
           x=x+2;
           count=count+1;
       }while(count<=10);
       System.out.println("Sum of first 10 even numbers is "+sum);

    }
    
}
