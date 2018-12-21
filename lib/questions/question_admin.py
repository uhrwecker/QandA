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

    def edit_answer_in_question(self, question_title, answer_index, entry, new_value):
        self.questions[question_title].edit_answer(answer_index, entry, new_value)

    def remove_answer_in_question(self, question_title, answer_index):
        self.questions[question_title].remove_answer(answer_index)

    def add_answer_in_question(self, question_title, answer_string='', comment='', 
                               is_correct=False):
        self.questions[question_title].add_answer(answer_string=answer_string, comment=comment,
                                                  is_correct=is_correct)

    def show_question(self, question_title):
        answer_index = self.questions[question_title].show_on_terminal()
        return answer_index

    def search(self, search=''):
        # right now, it only searches by title, which should be enough
        questions = []
        for title in self.questions.keys():
            if search in title:
                questions.append(self.questions[title])
        return questions

    def select_questions(self):
        # TODO introduce QuestionSelectHandler, that implements a more divers and
        #      substantial question selection algorithm
        qs = []
        for q in list(self.questions.values())[:5]:
            qs.append(q)
        return qs

    def get_data(self):
        data = []
        for q in self.questions.values():
            data.append(q.get())
        return data

