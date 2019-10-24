# Address Book (Python)
This is a basic address book that displays a menu where the user can add a contact, display all contacts that have been added, search for a contact by name, delete a specific contact, and save changes and exit the program. This program creates a .txt file on the user's computer that stores all contacts created by the program. The program runs as follows:

Step 1) The program reads in the .txt file and parses information to lists of first names, last names, numbers, emails, addresses, social media, and pets.

Step 2) Displays a menu for the user with the options: Add contact, display contact, search by name, delete, save and exit.
**** Add Contact -- asks for first name, last name, phone number, email address, street address, snapchat username, and favorite pet and appends all information given to the .txt file and returns to the menu

**** Display Contact -- displays all contacts in the .txt file to the console and returns to the menu.

**** Search by Name -- asks for the user to input the last name of a user and searches through the list of last names to find a matching result, which upon finding will output the first and last name of the contact along with their number, email, address, social media, and pet and return to the menu.

**** Delete -- asks for the user to input the index number associated with the contact they would like to delete from the address book. When the user inputs a valid number, the program will delete all information associated with the contact from the .txt file and return to the menu.

**** Save and Exit -- will overwrite the current .txt file with the information stored in the lists of the program, thereby adding it to the .txt file for the next time it is used. After the file is updated, the program will exit.
