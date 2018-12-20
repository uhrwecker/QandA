import logging

from lib.answers import answer

class QuestionInterface():
    '''
    Impl. of Question Interface; 
    '''
    def __init__(self, title='', category='Physik', question_string='', answers=[],
                 language='german'):
        assert title, 'The question must have a title'
        assert question_string, 'The question must have a question!!'
        assert answers, 'There must be a list of answer dictionairies'
        self.title = title
        self.category = category
        self.question_string = question_string
        self.answers = self._setup_answers(answers)
        # answers of form [{'answer': '...', 'comment' [optional]}, ]
        self.language = language

    def verify(self, given_answer_index):
        '''
        Implement this to check whether a given_answer is the right answer,
        and also give an explanation, why it might not be (answer_comment)
        '''
        raise NotImplementedError
    
    def add_answer(self, answer_string='', comment='', is_correct=False):
        self.answers.append(answer.Answer(answer_string=answer_string, comment=comment, 
                                          is_correct=is_correct))

    def remove_answer(self, answer_index):
        del self.answers[answer_index]

    def edit_answer(self, answer_index, entry, new_value):
        self.answers[answer_index].edit(entry, new_value)

    def set(self, entry, new_value):
        if entry == 'title':
            assert new_value and type(new_value) == str, 'Title must be string'
            self.title = new_value
        elif entry == 'category':
            assert new_value and type(new_value) == str, 'Category must be string'
            self.category = new_value
        elif entry == 'question_string':
            assert new_value and type(new_value) == str, 'Q.String must be string'
            self.question = new_value
        elif entry == 'language':
            assert new_value and type(new_value) == str, 'Language must be string'
            self.language = new_value
        else:
            raise ValueError('{} is not a field in Question!'.format(entry))

    def get(self):
        config = {}
        config['title'] = self.title
        config['category'] = self.category
        config['question_string'] = self.question_string
        config['answers'] = [d.get_config() for d in self.answers]
        config['language'] = self.language
        return config

    def show_on_terminal(self):
        print('--------------------------------------------')
        print('Next question:')
        print(self.question_string)
        print('--------------------------------------------')
        for answer, index in zip(self.answers, range(len(self.answers))):
            print('(' + str(index+1)  + ') ' + str(answer))
        return [answer_index for answer_index in range(len(self.answers))]


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
