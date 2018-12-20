import json

class FileHandlerJson():
    '''
    Handling .json files, saving, deleting, loading etc
    '''
    def __init__(self, path):
        self.path = path

    def load_data(self):
        fobj = open(self.path, 'r')
        config = json.load(fobj)
        fobj.close()
        return config

    def save_data(self, data):
        fobj = open(self.path, 'w')
        json.dump(data, fobj, indent=4, sort_keys=True)
        fobj.close()

    def change_path(self, path):
        self.path = path

    def save_dummy_data(self):
        q = {}
        q['title'] = 'The first question'
        q['question_string'] = 'Do you know how to setup a question?'
        q['answers'] = [{'answer_string': 'Just add one! You studip?'}]
        q['category'] = 'General'
        q['language'] = 'english'
        self.save_data([q])

def main():
    data = {'Hi': {'Im': 'Kevin'}}
    fhj = FileHandlerJson('./s.txt')
    fhj.save_data(data)
    data2 = fhj.load_data()
    assert data == data2
    fhj.change_path('./t.txt')
    fhj.save_data(data)

if __name__ == '__main__':
    main()
