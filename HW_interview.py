
class Stack:
    """описание класса"""
    def __init__(self, list_):
        """используемый список элементов"""
        self.list_ = list_

    def is_empty(self):
        """проверяет наличие элементов в списке"""
        return len(self.list_) == 0

    def push(self, add_element):
        """добавляет элемент в конец списка"""
        self.list_.append(add_element)

    def pop(self):
        """удаляет последний элемент списка и возвращает его"""
        del_element = self.list_[-1]
        self.list_ = self.list_[:-1]
        return del_element

    def peek(self):
        """возвращает последний элемент списка"""
        return self.list_[-1]

    def size(self):
        """возвращает количество элементов в списке"""
        return len(self.list_)



def check_balance_brackets(brackets: str) -> str:
    brackets = Stack(list(brackets))
    help_stack = Stack([])
    dict_ = {'(': ')', '{': '}', '[': ']'}
    for i in brackets.list_[::-1]:
        if i in dict_.values():
            help_stack.push(brackets.pop())
        elif help_stack.size() != 0 and help_stack.pop() == dict_[i]:
            brackets.pop()
        else:
            break

    if help_stack.is_empty() and brackets.is_empty():
        return "Сбалансированно"
    else:
        return "Неcбалансированно"















