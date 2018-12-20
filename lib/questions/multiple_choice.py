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
                result[index] = (self.answer[index].check_if_correct(), 
                                 getattr(self.answer[index], 'comment'))
        except:
            result[given_answer_index] = (self.answer[given_answer_index].check_if_correct(), getattr(self.answer[given_answer_index], 'comment'))

        return result



