using System;
namespace GestionBourget
{
	public class Contact
	{
		private String name;
		private string number;
		
		public Contact()
		{
		}

        public Contact(string name, string number)
        {
            this.name = name;
            this.number = number;
        }

        public string Name { get => name; set => name = value; }
        public string Number { get => number; set => number = value; }
    }
}

