class Stack:
    def __init__(self):
        self.stack_list =[]

    def is_empty(self):
        "is_empty - проверка стека на пустоту. Метод возвращает True или False."
        return bool(self.stack_list)

    def push(self, item):
        "push - добавялет новый элемент на вершину стека. Метод ничего не возвращает."
        self.stack_list.append(item)

    def pop(self):
        "pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека."
        self.stack_list.pop(-1)
        if self.peek() is not False:
            return self.stack_list[-1]
        else:
            pass

    def peek(self):
        "peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется."
        if self.is_empty() is True:
            return self.stack_list[-1]
        else:
            return False
    def size(self):
        "size - возвращает количество элементов в стеке."
        return len(self.stack_list)