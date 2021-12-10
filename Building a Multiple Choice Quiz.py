from Question import Question
question_prompts = [
    "What color are apples? \n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions =[                                 # create an array 
    Question(question_prompts [0], "a"),     # Question is class from Question.py file
    Question(question_prompts [1], "c"),
    Question(question_prompts [2], "b")

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:         # question.answer --> the "answer" comes from Quesetion.py file
            score += 1
    print("Your got " + str(score) + "/" +str(len(questions)) + " correct" )


run_test(questions)