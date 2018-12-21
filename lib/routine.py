from lib.questions import question_admin
from lib.util import filehandling
from lib.terminal import exam_env

class Routine():
    '''
    Main Routine that initializes and setup the questions, 
    saves and loads the questions;
    handles manipulations of questions;
    handles output
    '''
    def __init__(self, path):
        self.fh = filehandling.FileHandlerJson(path)
        self.save_data = self._handle_first_loading()
        self.qa = question_admin.QuestionAdmin(self.save_data)

        self.exam_env = exam_env.TerminalExamEnvironment()

    def show(self):
        for question in self.qa.questions:
            self.qa.show_question(question)

    def start_exam_env(self):
        questions = self.qa.select_questions()
        result = self.exam_env.start(questions)

    def save(self):
        self.fh.save_data(self.qa.get_data())

    def load(self, path=''):
        if path:
            self.fh.change_path(path)
        self.save_data = self.fh.load_data()
        self.qa = question_admin.QuestionAdmin(self.save_data)

    def search(self, search=''):
        questions = self.qa.search(search)
        self._show_search_results(questions, search)
        # there could be more later on, for now:
        # just show them on terminal

    def _show_search_results(self, questions, search):
        print('The search results are in; following questions have been found containing {}:'.format(search))
        for q in questions:
            print(str(q.title) + ' in category ' + str(q.category))

    def _handle_first_loading(self):
        try:
            return self.fh.load_data()
        except FileNotFoundError:
            self.fh.save_dummy_data()
            return self.fh.load_data()

