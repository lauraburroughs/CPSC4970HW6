# Laura Burroughs
# CPSC 4970
# 3 April 2026
# Project 4

class OddIterator:

    def __init__(self, it):
        self._it = iter(it)

    def __iter__(self):
        return self

    def __next__(self):

        while True:
            value = next(self._it)

            if value % 2 != 0:
                return value

class Last:

    def __init__(self, it, count):
        self.saved_list = []
        for x in it:
            self.saved_list.append(x)

            if len(self.saved_list) > count:
                self.saved_list.pop(0)

            if count < 0:
                raise ValueError # so you cannot have a negative count

        self.current_index = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.current_index >= len(self.saved_list):
            raise StopIteration

        value = self.saved_list[self.current_index]
        self.current_index += 1
        return value