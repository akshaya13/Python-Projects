date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to  10? ")
journal = input("Let your thoughts flow!: \n")

with open(f"{date}.txt", "w") as file:
    file.writelines(journal)

