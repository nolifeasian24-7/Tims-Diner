import java.util.Scanner;
class table {
    public void start() {
        try {

            Scanner scanner = new Scanner(System.in);//this is a scanner object (Basically an instance of a class, in OOP this is how you get multiple files joined together)
            System.out.println("Welcome to tims diner, please enter your table number or die");
            int var1 = scanner.nextInt();

            for (int i = 0;i < 10; i++) {

                if (var1 < 0 || var1 > 10) {
                    throw new Exception();
                } else {
                    System.out.println("well done");
                    break;
                }
    
            }

        } catch (Exception e) {
            System.out.println("Please enter your table number again");
            start();
        }
        
    }
}