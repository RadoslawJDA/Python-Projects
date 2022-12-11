from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for x in question_data:
    question_bank.append(Question(x['text'], x['answer']))


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print('You have completed the quiz')
print(f'Your score is: {quiz.score}/{quiz.question_number}')
