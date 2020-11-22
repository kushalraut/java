//Program No. 16 : Define a class, describe its constructor, 
//overload the Constructors and instantiate its object. 
public class Constructor{
    int  value1;
    int  value2;
    Constructor(){
     value1 = 10;
     value2 = 20;
    
   }
   Constructor(int a){
    value1 = a;
    
  }
  Constructor(int a,int b){
  value1 = a;
  value2 = b;
 
 }
 public void display(){
    System.out.println("Value1 === "+value1);
    System.out.println("Value2 === "+value2);
}
public static void main(String args[]){
  Constructor d1 = new Constructor();
  Constructor d2 = new Constructor(30);
  Constructor d3 = new Constructor(30,40);
  System.out.println("Inside default Constructor");
  d1.display();
  System.out.println("Inside paramaterized Constructor1");
  d2.display();
  System.out.println("Inside paramaterized Constructor2");
  d3.display();
}
}