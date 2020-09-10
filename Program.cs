using System;
using System.IO;

namespace TimsDinercs
{
    class Program : getFood 
    {
        public void table()
        {
            int Table;
            Console.Title = "Tim's diner";
            Console.ForegroundColor = ConsoleColor.Yellow;
            try
            {
                while (true) 
                {
                    Console.WriteLine("Welcome to tims diner, enter your table number");
                    Table = Convert.ToInt32(Console.ReadLine());
                    if (Table >10 || Table <0)
                    {
                        Console.WriteLine("Sorry, that table doesn't exist, please try again...");
                        continue;
                    }
                    else 
                    {
                        Console.WriteLine($"{Table} is your table number.");
                        getFood food1 = new getFood();
                        food1.food();
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Wrong type, please try again");
                table();
                
            }
        }
    }
}
