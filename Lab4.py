
"""
Plain English
This program allows a user three tries to guess the correct answer to the question
"What is the capital of California?" The answer is "Sacramento"

We first set max_tries = 3. Then we create a loop to iterate three times. For each iteration,
we ask the user for the answer (User input). Then based on the answer the User gives, we check
to see if the user input matches the answer. If so, print "Correct!", then terminate the 
loop with a break statement.

If the User cannot guess the correct answer within the max_tries, then print "You have used
up your allotment of guesses.", then print "The correct answer is Sacramento."

"""

"""
Pseudocode

main()
  question = "What is the capital of California?"
  answer = "Sacramento"
  ask(question, answer)

ask()
  tries = 0
  loop three times
    increment tries
    ask user input()
    check to see if user input is equal to answer
        if so, print "Correct", then break out of loop
  if not correct
    print to the user "You have used up your allotment of guesses."
    print the correct answer "The correct answer is 'Sacramento'."

main
"""



