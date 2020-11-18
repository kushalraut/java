//Program No.11: Display sum of first 10 even nos.using do-while loop. 
public class sum_even_nos {
public static void main(String args[])
{
int no=1,count=0,sum=0;
System.out.println("even number:");
while(count!=10)
{
if(no%2==0)
{
sum=sum+no;
count=count+1;
}
no++;
}
System.out.println("The sum of  first 10 even numbers is: "+sum);
}
}