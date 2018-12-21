from lib.questions import question_interface

class MultipleChoiceQuestion(question_interface.QuestionInterface):
    '''
    Impl. of Question Interface;
    Implements a multiple choice question;
    '''
    def __init__(self, title, category, question_string, answers=[], 
                 language='german'):
        super().__init__(title, category, question_string, answers=answers,
                         language=language)

    def verify(self, given_answer_index):
        result = {}
        try:
            for index in given_answer_index:
                index = int(index)
                result[index] = (self.answers[index].check_if_correct(), 
                                 getattr(self.answers[index], 'comment'))
        except:
            result[str(given_answer_index)] = (self.answers[given_answer_index].check_if_correct(), getattr(self.answers[given_answer_index], 'comment'))

        return result



