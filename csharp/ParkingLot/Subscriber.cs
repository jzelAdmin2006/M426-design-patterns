using System;
using System.Collections.Generic;
using System.Diagnostics.Tracing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ParkingLot
{
    public interface Subscriber
    {
        public void Update(EventArgs args);
    }
}
