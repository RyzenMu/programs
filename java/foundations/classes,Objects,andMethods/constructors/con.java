public class con{
    
    public static void main(String[] args){

        Student s1 = new Student(24, "MinerStone");
        s1.info();

    }
}

class Student{
    int rollno;
    String name;
    Student(int rollnoa, String namea){
        rollno = rollnoa;
        name = namea;
    }
    void info(){
        System.out.println("The name of the student is :" + name );
        System.out.println("The Roll No of the student is :" + rollno);
    }
}