using System;

namespace TimsDinercs
{
    class Program : getFood 
    {
        public void table()
        {
            Console.Title = "Tim's diner";
            Console.ForegroundColor = ConsoleColor.Yellow;
            while (true) 
            {
                int table;
                Console.WriteLine("Welcome to tims diner, enter your table number");
                table = Convert.ToInt32(Console.ReadLine());
                if (table >10 || table <0)
                {
                    Console.WriteLine("Sorry, that table doesn't exist, please try again...");
                    continue;
                }
                else 
                {
                    Console.WriteLine($"{table} is your table number.");
                    break;
                }
            }
            getFood food1 = new getFood();
            food1.food();
        }
    }
}
