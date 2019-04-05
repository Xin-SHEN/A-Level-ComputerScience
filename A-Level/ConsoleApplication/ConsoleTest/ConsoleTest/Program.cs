using System;

namespace ConsoleTest
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            string astr = "a string";
            int aint = 11;
            int bint = aint + 1;
            bint = AddOne(bint);

            Console.WriteLine("Hello World!"+ astr);
            Console.WriteLine(bint);
            Console.ReadLine();
        }

        static int AddOne(int input){
            return input + 1;
        }
    }
}
