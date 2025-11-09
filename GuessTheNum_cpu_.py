import random

def guesse(x):
    random_number = random.randint(1,x)
    guesse = 0
    while guesse != random_number:
        guesse = int(input(f"Guesse the number between 1 and {x} : "))
        if guesse < random_number:
            print("Your to low")
        elif guesse > random_number:
            print("Your to high")
            
    print("Wow, you get it, congrats")
    
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guesse = random.randint(low,high)
        else:
            guesse = low
        feedback = input(f"It's {guesse} correct (c), or too low (l), or too high (h)? ")
        if feedback == "h":
            guesse -= 1
        elif feedback == "l":
            guesse += 1
    
    print("You get it")


computer_guess(10)