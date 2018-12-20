import logging

from lib.answers import answer

class QuestionInterface():
    '''
    Impl. of Question Interface; 
    '''
    def __init__(self, title, category, question_string, answers,
                 answer_comments=[], language='german'):
        self.title = title
        self.category = category
        self.question_string = question_string
        self.answers = self._setup_answers(answers)
        # answers of form [{'answer': '...', 'comment' [optional]}, ]
        self.language = language

    def verify(self, given_answer):
        '''
        Implement this to check whether a given_answer is the right answer,
        and also give an explanation, why it might not be (answer_comment)
        '''
        raise NotImplementedError

    def edit_answer(self, answer_index, entry, new_value):
        self.answers[answer_index].edit(entry, new_value)


    def set(self, var, val):
        if var in self.__dict__:
            self.__dict__[var] = val
        #TODO normally, there should be n set - funcs

    @staticmethod
    def _setup_answers(answer_config):
        answers = []
        for setup in answer_config:
            answers.append(answer.Answer(**setup))

        return answers

def main():
    q = QuestionInterface('Hi', 'New', '', 'a')
    q.set(1, 2)

if __name__ == '__main__':
    main()
