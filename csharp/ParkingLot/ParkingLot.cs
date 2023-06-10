using System.Runtime.CompilerServices;
using System;

namespace ParkingLot
{
    public class ParkingLot : Publisher
    {
        public string Name { get; }
        public int Capacity { get; }
        public int Occupied { get; set; }
        private List<Subscriber> Subscribers = new();

        public ParkingLot(string name, int capacity)
        {
            this.Name = name;
            this.Capacity = capacity;
            this.Occupied = 0;
        }

        [MethodImpl(MethodImplOptions.Synchronized)]
        public void Enter()
        {
            if (Occupied < Capacity)
            {
                Occupied++;
                Publish(new LotChange("entered", Occupied, Capacity, Name));
            }
            else
            {
                throw new InvalidOperationException("parking lot is full");
            }
        }

        [MethodImpl(MethodImplOptions.Synchronized)]
        public void Exit()
        {
            if (Occupied > 0)
            {
                Occupied--;
                Publish(new LotChange("left", Occupied, Capacity, Name));
            }
            else
            {
                throw new InvalidOperationException("parking lot is empty");
            }
        }

        public void Subscribe(Subscriber subscriber)
        {
            Subscribers.Add(subscriber);
        }

        public void Publish(EventArgs args)
        {
            Subscribers.ForEach(subscriber => subscriber.Update(args));
        }
    }

    class LotChange : EventArgs
    {
        public string ChangeType { get; }
        public int Occupations { get; }
        public int Capacity { get; }
        public string LotName { get; }

        public LotChange(string changeType, int occupations, int capacity, string lotName) { 
            this.ChangeType = changeType;
            this.Occupations = occupations;
            this.Capacity = capacity;
            this.LotName = lotName;
        }
    }
}
