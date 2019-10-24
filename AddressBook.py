
firstNames = []
lastNames = []
numbers = []
emails = []
address = []
socialMedia = []
pet = []

inputFile = open("contactList.txt", "r")
contacts = inputFile.readlines()
inputFile.close()

for i in range(len(contacts)):
	pieces = contacts[i].split(";")
	firstNames.append(pieces[0].strip())
	lastNames.append(pieces[1].strip())
	numbers.append(pieces[2].strip())
	emails.append(pieces[3].strip())
	address.append(pieces[4].strip())
	socialMedia.append(pieces[5].strip())
	pet.append(pieces[6].strip())
	
menuChoice = "6"

while menuChoice != "0":

	menuChoice = (input("Please choose an option:\n1: Add contact\n2: Display Contact\n3: Search by name\n4: Delete\n0: Save and Exit\n"))

	if menuChoice == "1":
		firstNames.append(input("Enter the first name: "))
		lastNames.append(input("Eneter the last name: "))
		numbers.append(input("Enter the number: "))
		emails.append(input("Enter the email address: "))
		address.append(input("Enter the street address: "))
		socialMedia.append(input("Enter the snapchat username: "))
		pet.append(input("Favorite pet: "))
		print("Contact added\n")

	elif menuChoice == "2":
		print ("\n\n")
		for i in range(len(firstNames)):
			print(str(i+1) + ".")
			print("  " + firstNames[i] + " " + lastNames[i])
			print("\t" + numbers[i])
			print("\t" + emails[i])
			print("\t" + address[i])
			print("\t" + socialMedia[i])
			print("\t" + pet[i] + "\n")
			
	elif menuChoice == "3":
		print("Please enter last name to search for: ")
		lastName = input()
		for i in range(len(lastNames)):
			if lastName == lastNames[i]:
				print("\n" + "  " + firstNames[i] + " " + lastNames[i])
				print("\t" + numbers[i])
				print("\t" + emails[i])
				print("\t" + address[i])
				print("\t" + socialMedia[i])
				print("\t" + pet[i] + "\n")
			
	elif menuChoice == "4":
		for i in range(len(lastNames)):
			print("Contacts : " + str(i + 1) + " " + lastNames[i])		
		print("What contact would you like to delete?" )
		nameToDelete = int(input())-1
		del firstNames[nameToDelete]
		del lastNames[nameToDelete]
		del numbers[nameToDelete]
		del emails[nameToDelete]
		del address[nameToDelete]
		del socialMedia[nameToDelete]
		del pet[nameToDelete]
		print("\n")
		
outputFile = open("contactList.txt", "w")
for i in range(len(firstNames)):
	outputFile.write(firstNames[i] + "; " + lastNames[i] + "; " + numbers[i] + "; " + emails[i] + "; " + address[i] + "; " + socialMedia[i] + "; " + pet[i] + "\n")