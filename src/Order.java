import java.util.Scanner;
import java.util.HashMap;
import java.util.ArrayList;
class Order extends table {
    

    public void startOrder() {
        Scanner food = new Scanner(System.in);
        System.out.print("Enter you order split by a , :");
        String[] result = food.nextLine().split(",");
        ArrayList<Integer> validOrders = new ArrayList<>();
        HashMap<String, Integer> foodItems = new HashMap<>();
        foodItems.put("BTS MILKSHAKE", 420);
        foodItems.put("DNA Burgers", 69);
        foodItems.put("Samsung Galaxy S20 Plus BTS Edition", 999);
        Boolean scrap1 = true;

        for (int i = 0; i != result.length; i++) {
            try {
                Integer orderNumber = Integer.valueOf(result[i]);
                if (orderNumber < 0 || orderNumber > 3) {
                    System.out.println("Sorry, please enter your order items again");
                    startOrder();
                }
                else {
                    System.out.println("Verified");
                    validOrders.add(orderNumber);
                    scrap1 = false;
                    continue;
                }
                if (scrap1 = false){
                    start();
                }

            } catch (Exception e) {
                System.out.println("USE NUMBERS BIG STUPID");
                startOrder();
            }
        }
         
    }


}