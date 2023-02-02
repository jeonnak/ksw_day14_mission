"""

10.4 name, symbol, number 인스턴스 속성 가진
 Element 클래스를 만들어보자.
 이 클래스에서 'Hydrogen', 'H', 1 값을 가진 객체를 생성한다.

10.5 'name' : 'Hydrogen', 'symbol' : 'H', 'number' : 1과 같이
 키와 값으로 이루어진 el_dict 딕셔너리를 만들어보자.
 그리고 el_dict 딕셔너리로부터 Element 클래스의 hydrogen 객체를 생성한다.

10.6 Element 클래스에서 객체의 속성 (name, symbol, number) 값을
 출력하는 dump() 메서드를 정의한다. 이 클래스의 hydrogen 객체를
 생성하고, dump() 메서드로 이 속성을 출력한다.

"""

# name, symbol, number 인스턴스 속성 가진 Element 클래스 생성
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

 # name, symbol, number 속성의 값을 출력하는 dump() 메서드

    def dump(self):
        print(self.name, self.symbol, self.number)

# Element 클래스에서 'Hydrogen','H', 1 값 가진 객체 produce 생성

produce = Element('Hydrogen','H', 1)
print(produce.name, produce.symbol, produce.number)

# 'name' : 'Hydrogen', 'symbol' : 'H', 'number' : 1과 같이
#  키와 값으로 이루어진 el_dict 딕셔너리 생성

el_dict = {'name' : 'Hydrogen', 'symbol' : 'H', 'number' : 1}

# el_dict 딕셔너리로부터 Element 클래스의 hydrogen 객체를 생성

hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
print(hydrogen.name, hydrogen.symbol, hydrogen.number)

# dump() 메서드 출력
hydrogen.dump()
