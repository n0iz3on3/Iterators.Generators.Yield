
class FlatIteratorS:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.chek_list = sum(self.list_of_list, [])
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.chek_list) == self.cursor:
            raise StopIteration
        else:
            return self.chek_list[self.cursor]