from stack import Stack

print("\n\nLet's Play Towers of Hanoi\n\n")

# Creating the stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Setting up the game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("\nEnter a number greater than or equal to 3\n"))

for i in range(num_disks, 0, -1):
    left_stack.push(i)

num_optimal_moves = (2 ** num_disks) - 1
print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))


# Getting user input
def get_input():
    choices = [stack_.get_name()[0] for stack_ in stacks]

    while True:
        for j in range(len(stacks)):
            name = stacks[j].get_name()
            letter = choices[j]

            print("Enter {0} for {1}".format(letter, name))

        user_input = input("").upper()
        if user_input in choices:
            for n in range(len(stacks)):
                if user_input == choices[n]:
                    return stacks[n]


# Playing the game
num_user_moves = 0
while right_stack.get_size() != num_disks:
    print("\n\n...Current Stacks...")

    for stack in stacks:
        stack.print_items()

    while True:
        print("\nWhich stack do you want to move?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        if from_stack.size == 0:
            print("\n\nInvalid Move. Try Again")
        elif to_stack.size == 0 or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again")

print("\n\nYou completed the game i {0} moves, and the optimal number of moves is {1}".
      format(num_user_moves, num_optimal_moves))
