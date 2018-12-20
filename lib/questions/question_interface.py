import logging

class QuestionInterface():
    '''
    Impl. of Question Interface; 
    '''
    def __init__(self, title, category, question_string, answers, 
                 right_answer=1, answer_comments=[], language='german'):
        self.title = title
        self.category = category
        self.question_string = question_string
        self.answers = answers
        self.right_answer = right_answer
        self.answer_comment = answer_comments
        self.language = language

    def verify(self, given_answer):
        '''
        Implement this to check whether a given_answer is the right answer,
        and also give an explanation, why it might not be (answer_comment)
        '''
        raise NotImplementedError

    def set(self, var, val):
        if var in self.__dict__:
            self.__dict__[var] = val
        #TODO normally, there should be n set - funcs

def main():
    q = QuestionInterface('Hi', 'New', '', 'a')
    q.set(1, 2)

if __name__ == '__main__':
    main()
