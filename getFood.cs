using System;
using System.IO;

namespace TimsDinercs
{
    class getFood
    {
        public void food()
        {
            string[] foodItems = 
            {
                "Urio special",
                "@spicychair",
                "BTS DNA milkshake",
                "literally food",
                "Y",
                "Me when food"
            };
            Console.WriteLine("How many items would you like to order");
            int size = Convert.ToInt32(Console.ReadLine());
            int[] ordersize = new int[size];
            System.IO.StreamWriter food = new System.IO.StreamWriter(@"C:/Users/akuri/Documents/TimsDinercs/ food.txt");
            for (int i = 0; i !=size;i++)
            {
                if (i != size)
                {
                    Console.WriteLine("Enter your order items");
                    string userOrder = Console.ReadLine();
                    Console.WriteLine(Array.Exists(foodItems, element => element == userOrder));
                    food.WriteLine(userOrder);
                    food.Flush();
                }
                //This Logic statement is not working at the present moment, the reason probably being down to some structure fail in the for loop
            }
            food.Close();
            ReadFile fileRead = new ReadFile();
            fileRead.readFile();
        }
    }
}