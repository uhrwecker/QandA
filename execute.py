from lib import routine

def main():
    question_1 = {}
    question_1['title'] = 'The first question'
    question_1['question_string'] = 'Do you know how to add a question?'
    question_1['answers'] = [{'answer_string': 'Yes my lord'}]
    question_1['category'] = 'None'
    mr = routine.Routine('./save.txt')
    mr.show()

if __name__ == '__main__':
    main()
