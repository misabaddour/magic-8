import random

name = "Mikhail"
question = "Will I be able to win the competition?"
answer = ""

random_number = random.randint(1, 9)

if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    nswer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubful"
else:
    answer = "Error"

if len(name) == 0:
    print("The name is empty")
elif len(question) == 0:
    print("The question is empty")
else:
    print(name + " asks: " + question)
    print("Magic 8 Ball's answer: " + answer)
