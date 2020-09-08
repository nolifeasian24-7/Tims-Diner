using System;
using System.IO;

namespace TimsDinercs
{
    class getFood
    {
        public void food()
        {
            bool fileClosed = false;
            string[] foodItems = 
            {
                "BTS",
                "O no spaghetti",
                "Samsung galaxy Note 20 ultra",
                "Am1_mk4 #2087 (Get at my discord thank you :))",
                "Ti-84 graphing calculator",
                "Y"
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
                else if (i == size)
                {
                    ReadFile read = new ReadFile();
                    read.readFile();

                }
            }
        }
    }
}