from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if not self.__len__():
            return None

        return self._data.pop(0)

    def search(self, index):
        if index < 0 or index > self.__len__() - 1:
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]

    def is_empty(self):
        return not len(self._data)

    def get_element_at(self, index):
        if index > len(self._data) - 1:
            return None

        return self._data[index]
