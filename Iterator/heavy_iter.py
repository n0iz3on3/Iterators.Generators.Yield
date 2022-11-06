
class FlatIteratorH:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_iter = iter(self.list_of_list)
        self.chek_list = [self.list_iter]
        return self

    def __next__(self):
        while self.chek_list:
            try:
                element = next(self.chek_list[-1])
            except StopIteration:
                self.chek_list.pop()
                continue
            if isinstance(element, list):
                self.chek_list.append(iter(element))
                continue
            else:
                return element
        raise StopIteration