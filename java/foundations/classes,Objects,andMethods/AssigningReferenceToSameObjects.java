public class AssigningReferenceToSameObjects {
    public static void main(String[] args)
    {
        System.out.println("hello");

        Rectangle r = new Rectangle();
        r.length = 10;
        System.out.println((r.length));
        Rectangle r2 = r;
        r2.length = 20;
        System.out.println((r2.length));

    }
}

class Rectangle
{
    int width;
    int length;
    int area()
    {
        int a = width * length;
        return a;
    }
}