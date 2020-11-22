//Program No. 17: Illustrate method of overloading

public class Overloading {

    double   result ;
    double area(int a)
    {
        result = 3.14* a * a ;
        return result;
    }
    double area(int a , int b)
    {
        result = a * b;
        return result;
    }
    double area(int a , int b , int c)
    {
        result = a *b *c;
        return result;
    }

   
    
    public static void main(String[] args) {
         Overloading m1 = new Overloading();
        double  a,b,c;
        a=m1.area(2);
        System.out.println("area of circle is " + a);
        b=m1.area(2,3);
        System.out.println("area of rectangle is "+b);
        c= m1.area(2,3,5);
        System.out.println("volume of cuboid is "+ c);
       

    }
}