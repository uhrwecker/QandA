from lib.questions import multiple_choice

class QuestionAdmin():
    '''
    Class that handles the setup, order and 
    overall behavior of questions
    '''
    def __init__(self, question_config):
        self.questions = {}
        self._setup_questions(question_config)

    def _setup_questions(self, config):
        questions = {}
        for setup in config:
            question_class = setup.pop('type', 'MultipleChoiceQuestion')
            self.add_question(question_class, **setup)
        return questions

    def add_question(self, question_class, **config):
        try: 
            self.questions[config['title']] = multiple_choice.__dict__[question_class](**config)
        except:
            raise ImportError('No {} in specified import list!'.format(question_class))

    def delete_question(self, question_title):
        del self.questions[question_title] 

    def edit_question(self, question_title, entry, new_value):
        assert question_title in self.questions, 'Question not found.'
        question = self.questions[question_title]
        question.set(entry, new_value)
        del self.questions[question_title]
        self.questions[question.title] = question

    #def edit_answer_in_question(self, question_title,
