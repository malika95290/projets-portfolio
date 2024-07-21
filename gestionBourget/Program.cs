using System;
using System.Collections.Generic;
using GestionBourget;

internal class Program
{
    private static void Main(string[] args)
    {
        List<Company> companies = new List<Company>();

        void displayMenu()
        {
            Console.Clear();
            Console.WriteLine("################");
            Console.WriteLine("#Gestion Bourget#");
            Console.WriteLine("################");
            Console.WriteLine("1 - Saisir un emplacement");
            Console.WriteLine("2 - Saisir une entreprise");
            Console.WriteLine("3 - Saisir un contact");
            Console.WriteLine("4 - Afficher les exposants");
            Console.WriteLine("0 - Quitter l'application");

        }

        //Saisir entreprise
        void inputCompany()
        {
            Console.Clear();
            Console.WriteLine("Saisir un numéro de SIRET (14 chiffres)");
            string siret = Console.ReadLine() ?? "";

            //On vérifie le siret
            if (siret.Length != 14)
            {
                Console.WriteLine("Numéro de siret invalide. Appuyer sur entrer pour retourner au mne principal.");
                return;
            }

            Console.WriteLine("Saisir un nom");
            string name = Console.ReadLine() ?? "";

            Company newCompany = new Company(siret, name);
            companies.Add(newCompany);


            //Ajout de l'emplacement
            Placement placement = inputPlacement();
            newCompany.SetPlacement(placement);

            Console.WriteLine("Entreprise ajoutée avec succès. Appuyer sur entrer pour retourner au menu.");
      
        }

        //Saisi contact
        void inputContact()
        {
            Console.Clear();
            Console.WriteLine("Saisir un nom: ");
            string name = Console.ReadLine() ?? "";
            string number;

            //Vérification du numéro de téléphone
            while (true)
            {
                Console.WriteLine("Saisir un numéro de téléphone (10 chiffres) : ");
                number = Console.ReadLine();
                if (number.Length != 10)
                {
                    Console.WriteLine("Numéro de téléphone invalide. Veuillez saisir un numéro de téléphone à 10 chiffres.");
                }
                else
                {
                    break;
                }
            }

           
            bool companyExists = false;

            //On vérifie si l'entreprise associée existe
            while (!companyExists)
            {
                Console.WriteLine("Nom de l'entreprise associée au contact : ");
                string nameCompany = Console.ReadLine();

                foreach (var company in companies)
                {
                    if (company.Name == nameCompany)
                    {
                        Contact contact = new Contact(name, number);
                        company.AddContact(contact);
                        companyExists = true;
                        Console.WriteLine("Contact ajouté avec succès. Appuyer sur entrer pour retourner au menu principal.");
                        break;
                    }
                }

                if (!companyExists)
                {
                    Console.WriteLine("Entreprise non trouvée. Veuillez saisir un nom d'entreprise valide ou tapez 1 pour retournez au menu principal");
                    string choice = Console.ReadLine();
                    if (choice == "1")
                    {
                        return;
                    }
                }
            }
        }


        // Saisi emplacement
        Placement inputPlacement()
        {
            Console.Clear();
            Console.WriteLine("Saisir le hall : ");
            string hall = Console.ReadLine() ?? "";
            Console.WriteLine("Saisir la parcelle : ");
            int parcel = int.Parse(Console.ReadLine() ?? "0");
            Console.WriteLine("Saisir la surface (en m2) : ");
            int surface = int.Parse(Console.ReadLine() ?? "0");
            return new Placement(hall, parcel, surface); 
        }

        //Affichage de tous les exposants
        void displayExposant()
        {
            Console.WriteLine("Liste des exposants : ");
            foreach (var company in companies)
            {
                company.DisplayInfo();
            }
        }

        bool menuOn = true;

        while (menuOn)
        {
            displayMenu();
            int userEntry = int.Parse(Console.ReadLine());
            switch (userEntry)
            {
                case 1:
                    inputPlacement();
                    Console.Read();
                    break;
                case 2:
                    inputCompany();
                    Console.Read();
                    break;
                case 3:
                    inputContact();
                    Console.Read();
                    break;
                case 4:
                    displayExposant();
                    Console.Read();
                    break;
                case 0:
                    menuOn = false;
                    break;

            }
        }



    }
}
