from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        else:
            raise IndexError("Não há elementos")

    def search(self, index):
        if index not in range(len(self.data)):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.data[index]

    def is_empty(self):
        return len(self.data) == 0

    def remove(self):
        try:
            self.dequeue()
            print("Arquivo removido com sucesso.")
        except IndexError as e:
            raise e
