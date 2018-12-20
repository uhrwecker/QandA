from lib.questions import question_admin
from lib.util import filehandling

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

    def show(self):
        for question in self.qa.questions:
            self.qa.show_question(question)


    def _handle_first_loading(self):
        try:
            return self.fh.load_data()
        except FileNotFoundError:
            self.fh.save_dummy_data()
            return self.fh.load_data()

