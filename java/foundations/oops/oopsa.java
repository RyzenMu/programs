class Pen {
    String color;
    String type;

    public void write(){
        System.out.println("writing Something");
    }

    public void printColor(){
        System.out.println(this.color);
    }

}





public class OOPS {

    public static void main(String[] args){
        Pen pen1 = new Pen();
        pen1.color = " Black ";
        pen1.type = "Ball Point";
        pen1.write();
    }

}