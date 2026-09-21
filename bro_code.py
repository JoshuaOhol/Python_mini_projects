#python quiz game

questions = ("how many elements in the periodic table?: ",
            "which animal lays the largest egg?: ",
            "the most abundant gas in the Earth's atmosphere?: ",
            "how many bones in human body?: ",
            "which planet is the hottest in the solar system?: ")

options = (("A. 116","B. 117","C. 118","D. 119"),
          ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
          ("A. Nitrogen","B. Oxygen","C. Cardon-Dioxide","D. Hydrogen"),
          ("A. 205", "B. 210","C. 211","D. 202"),
          ("A. Mercury","B. Venus","C. Earth","D. Mars"))

answers = ("C", "D", "A", "A", "B")

guesses = []
score = 0
question_num = 0

for question in questions:
  print("----------------------------------")
  print(question)
  for option in options[question_num]:
       print(option)

  guess = input("Enter (A,B,C,D): ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
        score +=1
        print("CORRECT ANSWER")
  else:
        print("INCORRECT ANSWER")
        print(f"{answers[question_num]} is the correct answer")
  question_num += 1

print("----------------------------------")
print("             RESULTS              ")
print("----------------------------------")

print("answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is : {score}%")