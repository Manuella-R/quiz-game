questions = (
    "How many continents are in the world: ",
    "How many wonders are there in the world: ",
    "Which is the youngest country in the world: ",
    "Which bird has the smallest brain: ",
    "What is the largest animal in the world: "
)

options = (
    ("A. 5", "B. 6", "C. 7", "D. 8"),
    ("A. 5", "B. 7", "C. 9", "D. 11"),
    ("A. South Sudan", "B. Kosovo", "C. East Timor", "D. Palau"),
    ("A. Ostrich", "B. Hummingbird", "C. Crow", "D. Sparrow"),
    ("A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Great White Shark")
)

answers = ("C", "B", "A", "B", "B")

guesses = []
score = 0
question_num=0

for question in questions:
    print("*********************")
    print(question)
    for option in options[question_num]:
        print(option)

    guess=input("Enter(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score +=1
        print("CORRECT")
    else: 
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("--------------------")
print("    Results         ")  
print("--------------------")   

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/ len(questions)*100)
print(f"Your score is: {score}%")