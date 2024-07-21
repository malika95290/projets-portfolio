using System;
namespace GestionBourget
{
	public class Placement
	{
		private string hall;
		private int parcelle;
		private int surface;

		public Placement()
		{
		}

        public Placement(string hall, int parcelle, int surface)
        {
            this.hall = hall;
            this.parcelle = parcelle;
            this.surface = surface;
        }

        public string Hall { get => hall; set => hall = value; }
        public int Parcelle { get => parcelle; set => parcelle = value; }
        public int Surface { get => surface; set => surface = value; }
    }
}

