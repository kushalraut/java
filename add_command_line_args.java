//Program No.15: Read and display the numbers 
//as command line Arguments and display the addition of them 

public class add_command_line_args {
    public static void main(String args[]) {
        int c=0;
        for(int i=0;i<args.length;i++)

        {
                    c=c + Integer.parseInt(args[i]);
            
        }
         System.out.println("The result is:"+c);
    }
}