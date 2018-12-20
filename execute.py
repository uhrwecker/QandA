from lib.questions import question_interface

def main():
    q = question_interface.QuestionInterface('The first one', 'Dummy', 
            '', [{'answer_string': 'THe first answer eva'}])
    print(q, q.__dict__)
    q.edit_answer(0, 'comment', 'This one is newwww')
    for item in q.__dict__.values():
        print(item)
    for ans in q.answers:
        print(ans)

if __name__ == '__main__':
    main()
