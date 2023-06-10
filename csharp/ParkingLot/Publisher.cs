using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ParkingLot
{
    public interface Publisher
    {
        void Subscribe(Subscriber subscriber);
        void Publish(EventArgs args);
    }
}
