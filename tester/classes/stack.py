class Stack:
    def __init__(self, data:list):
        self.data = data

    def push(self, item:int):
        self.data.append(item)

    def pop(self) -> int:
        top_index = len(self.data) - 1
        num = self.data[top_index]
        del(self.datap[top_index])
        return num

    def get_data(self):
        return self.data.copy()

    def __len__(self):
        return (len(self.data))
