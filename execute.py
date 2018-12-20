from lib.questions import question_admin

def main():
    question_1 = {}
    question_1['title'] = 'The first question'
    question_1['question_string'] = 'Do you know how to add a question?'
    question_1['answers'] = [{'answer_string': 'Yes my lord'}]
    question_1['category'] = 'None'
    q = question_admin.QuestionAdmin([question_1])
    print(q, q.__dict__)
    question_2 = question_1
    question_2['title'] = 'The second question'
    q.add_question('MultipleChoiceQuestion', **question_2)
    print(q, q.__dict__)

if __name__ == '__main__':
    main()
