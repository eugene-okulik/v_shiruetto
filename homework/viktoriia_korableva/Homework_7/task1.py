rl_number = 64
ent_number = int(input('Enter the number from 1 to 100: '))
while ent_number != rl_number:
    print("Please, try again")
    ent_number = int(input("Enter the number from 1 to 100: "))
print("Congratulations, you win")