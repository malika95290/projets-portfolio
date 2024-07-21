using System;
namespace GestionBourget
{
	public class Company
	{
        private string siret;
        private string name;
        public Placement Placement { get; private set; }
        private List<Contact> contacts = new List<Contact>();

        public string Siret { get => siret; set => siret = value; }
        public string Name { get => name; set => name = value; }
        public List<Contact> Contacts { get => contacts; } // Accesseur pour la liste de contacts


        public Company()
        {
        }

        public Company(string siret, string name)
        {
            this.siret = siret;
            this.name = name;
        }

        //Ajouter contact
        public void AddContact(Contact contact)
        {
            contacts.Add(contact);
        }

        //Modifier l'emplacement
        public void SetPlacement(Placement placement)
        {
            Placement = placement;
        }

        //Affichage info entreprise
        public void DisplayInfo()
        {
            Console.WriteLine($"Nom de l'entreprise : {Name}");
            Console.WriteLine($"Siret de l'entreprise : {Siret}");
            Console.WriteLine("Contacts:");
            foreach (var contact in Contacts)
            {
                Console.WriteLine($"Nom du contact : {contact.Name} - Numéro de téléphone : {contact.Number}");
            }
            Console.WriteLine("Hall : " + Placement.Hall + " - Parcelle : " +Placement.Parcelle + " - Surface : " + Placement.Surface +"m2");
            Console.WriteLine("----------------------");
        }

    }
}

