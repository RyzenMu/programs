class Calc {
    public void message(){
        System.out.println("Today is April");
    }
}

public class varArgs{
    public static void main(String[] args){
        System.out.println(90);
        Calc c1 = new Calc();
        System.out.println(c1.message());
    }
}