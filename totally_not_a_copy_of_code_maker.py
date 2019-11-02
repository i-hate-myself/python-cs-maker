c = 0

filename1 = input("input your file name: ")

filename2 = filename1 + """.cs"""

with open(filename2, "a") as myfile:
    myfile.write("""
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace """ + filename1 + """
{
    class Program
    {
        static void Main(string[] args)
        {
            
""")
    while True:
        x = input("press 1 to declare a fuction\n 2 for an if statement\n 3 for an else if statement \n 4 for a else statement \n 5 for a writeline statement \n 6 to declare a variable \n 7 for a random int statement \n 8 for a switch statement \n 9 read statement \n 10 for date and time \n 11 to see how many brackets you need to close \n 12 to add a bracket \n ")
        if x == "1":
            y = input("enter the name of your function: ")
            myfile.write("\n public void" + y + "() \n { \n")
            c += 1
        elif x == "2":
            myfile.write("\nif()\n{")
            c += 1
        elif x == "3":
            myfile.write("\nelse if()\n{")
            c += 1
        elif x == "4":
            myfile.write("\nelse\n{")
            c += 1
        elif x == "5":
            myfile.write("\nConsole.WriteLine();\n")
        elif x == "6":
            while True:
                z = input("input the type of variable you want \n 1 for int \n 2 for string\n 3 for bool\n 4 for float\n: ")
                if z == "1":
                    q = input("input the name of your variable: ")
                    myfile.write("int " + q + ";")
                elif z == "2":
                    q = input("input the name of your variable: ")
                    myfile.write("string " + q + ";")
                elif z == "3":
                    q = input("input the name of your variable: ")
                    myfile.write("bool " + q + ";")
                elif z == "4":
                    q = input("input the name of your variable: ")
                    myfile.write("float " + q + ";")
                else:
                    break
        elif x == "7":
            num1 = int(input("input your lowest value for your random class: "))
            num2 = int(input("input your highest value for your random class: "))
            randomname = input("input your random functions name: ")
            myfile.write("""Random rnd = new Random(); \n int """ + randomname + """ = rnd.Next(""" + num1 + ", " + num2 + """);""")
        elif x == "8":
            myfile.write(""" switch (caseSwitch)
            {
            case 1:

            case 2:

            default:
            """)
            c += 1
        elif x == "9":
            myfile.write("Console.Readline();")
        elif x == "10":
            myfile.write("DateTime.now")
        elif x == "11":
            print(" you need to close of " + str(c) + " bracket's")
        elif x == "12":
            myfile.write("}")
            c -= 1
        else:
            break
    myfile.write("""
        
        }
    }
}
""")

    myfile.close()

input()
