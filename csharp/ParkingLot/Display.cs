using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ParkingLot
{
    public class Display : Subscriber
    {
        public void Update(EventArgs args)
        {
            LotChange? change = args as LotChange; 
            if(change != null)
            {
                string changeType = change.ChangeType;
                int occupations = change.Occupations;
                int capacity = change.Capacity;
                string lot = change.LotName;
                Console.WriteLine($"A car {changeType} the lot '{lot}': {occupations}/{capacity} occupied.");
            }
        }
    }
}
