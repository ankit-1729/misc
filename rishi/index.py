class Question:
    def __init__(self, question_no):
        self.question_no = question_no
        self.isAttempted = False
        self.correctAnswer = ''
        self.providedAnswer = ''

    def isProvidedAnswerCorrect(self):
        return self.isAttempted and self.providedAnswer == self.correctAnswer


def getCenterJustifiedStr(str, width):
    return str.center(width, ' ')


def printStatRow(q, hidden):
    print('| {} | {} | {} | {} |'.format(getCenterJustifiedStr(str(q.question_no), 15),
                                         getCenterJustifiedStr('Yes' if q.isAttempted else 'No', 15), getCenterJustifiedStr(q.providedAnswer if q.providedAnswer else '-', 15), getCenterJustifiedStr('<Hidden>' if hidden else q.correctAnswer, 15)))
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


def printStats(questions, hidden=False):
    print('')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

    print('| {} | {} | {} | {} |'.format(getCenterJustifiedStr('Question No', 15),
                                         getCenterJustifiedStr('Attempted', 15), getCenterJustifiedStr('Provided Answer', 15), getCenterJustifiedStr('Correct Answer', 15)), sep='')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

    for q in questions:
        printStatRow(q, hidden)

    print('', end='\n\n')


def constructQuestionsArr(n):
    questions = []

    i = 0

    while i < n:
        questions.append(Question(i + 1))
        i += 1

    return questions


def getAnswerKeyInput(n, questions):
    print("Provide the 'Answer Key' as an input.")

    answers = input(
        'For each of the {} questions, provide space separated values (Eg. a b c) as the correct answers : '.format(n)).split(' ')

    i = 0

    while i < n:
        questions[i].correctAnswer = answers[i]
        i += 1


def computeNoOfAttemptedQuestions(questions):
    count = 0

    for q in questions:
        if q.isAttempted == True:
            count += 1

    return count


def computeNoOfCorrectlyAnsweredQuestions(questions):
    count = 0

    for q in questions:
        if q.isProvidedAnswerCorrect():
            count += 1

    return count


# def computeGrade(questions):
#     return 'A'


def computeFinalScoreStats(questions):
    print('')
    print('The Final Exam sheet is as follows : ', end='\n')
    printStats(questions)

    noOfCorrectlyAnsweredQuestions = computeNoOfCorrectlyAnsweredQuestions(
        questions)

    print('Exam Stats : ')
    print('Total number of questions : ', len(questions))
    print('Number of Attempted questions : ',
          computeNoOfAttemptedQuestions(questions))
    print('Number of correctly answered questions : ',
          noOfCorrectlyAnsweredQuestions)
    print('Percentage : ', round(
        (noOfCorrectlyAnsweredQuestions / len(questions)) * 100, 2))
    print('')

    # print('Grade : ', computeGrade(noOfCorrectlyAnsweredQuestions))


n = int(input('Enter the total number of questions : '))
print('')

questions = constructQuestionsArr(n)

getAnswerKeyInput(n, questions)

print('The Answer Key has been successfully saved.', end='\n\n')

print('You can now provide an answer to each of the {} questions one by one.'.format(n))
print('You have the following choices for each of the questions you want to give an answer to ....', end='\n')
print("1). To save a response to a question, enter 'R 1 c' (without quotes) where 1 is the question number and c is the answer choice")
print("2). To see the current status of the exam sheet, enter 'P' (without quotes)")
print("3). To end the exam and display the final score stats, enter 'E' (without quotes)")
print('')

while True:
    ipt = input('Enter your choice : ').split(' ')

    choice = ipt[0]

    if choice == 'P':
        print('')
        print('Printing the current status of the exam sheet ....', end='\n')
        printStats(questions, True)
    elif choice == 'E':
        computeFinalScoreStats(questions)
        break
    elif choice == 'R':
        q_no = int(ipt[1]) - 1
        q_ans = ipt[2]

        questions[q_no].isAttempted = True
        questions[q_no].providedAnswer = q_ans
    else:
        print('Invalid choice !! Please retry')

print('End Of Program !!')
