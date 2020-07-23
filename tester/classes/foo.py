class Foo:
    def __init__(self, con=None, service=None):
        self.db = con
        self.serivce = service

    def get_data(self):
        return self.db.get_data()

    def set_data(self, data):
        self.db.save_data(self, data)

    def process_data(self, string):
        return self.serivce.process_data(string)
