class DbConnection:
    def __init__(self):
        self.itr = 0
        self.data = {}
    def get_data(self):
        return self.data
    def save_data(self, object):
        self.data[self.itr] = object
        self.itr += 1