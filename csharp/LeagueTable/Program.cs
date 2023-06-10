using System;
using static LeagueTable.TableRow;

namespace LeagueTable
{
    class Program
    {
        static void Main(string[] args)
        {
            TableRow liverpool = new TableRowBuilder()
                .TeamName("Liverpool")
                .Build();
            TableRow arsenal = new TableRowBuilder()
                .TeamName("Arsenal London")
                .Rank(2)
                .Defeats(1)
                .GoalsConceded(3)
                .Build();

            Console.WriteLine(
                $"{"Team",20} {"#",2} {"W",2} {"D",2} {"T",2} {"+",2} {"-",2} {"=",2} {"P",2}"
            );
            Console.WriteLine(liverpool);
            Console.WriteLine(arsenal);
        }
    }
}
