"""
10.8 Element 클래스를 수정해서 name, symbol, number의 속성을
 private로 만든다. 각 속성값을 반환하기 위해 getter 프로퍼티를 정의한다.
"""

# name, symbol, number 인스턴스 private 속성 가지도록 Element 클래스 수정
class Element():
    def __init__(self, name, symbol, number):
        self.hidden__name = name
        self.hidden__symbol = symbol
        self.hidden__number = number

    @property
    def name(self):
        print('getter')
        return self.hidden__name

    @name.setter
    def name(self, name):
        print('setter')
        self.hidden__name = name

    @property
    def symbol(self):
        print('getter')
        return self.hidden__symbol

    @symbol.setter
    def symbol(self, symbol):
        print('setter')
        self.hidden__symbol = symbol

    @property
    def number(self):
        print('getter')
        return self.hidden__number

    @number.setter
    def number(self, number):
        print('setter')
        self.hidden__number = number

produce = Element('Hydrogen', 'H', 1)
produce.name
produce.symbol
produce.number