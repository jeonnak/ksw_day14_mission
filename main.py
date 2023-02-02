"""
10.7
print(hydrogen)을 호출한다. Element 클래스의 정의에서 dump 메서드를
 __str__() 메서드로 바꿔서 새로운 hydrogen 객체를 생성하고,
 그리고 print(hydrogen)을 다시 호출한다.
"""

# name, symbol, number 인스턴스 속성 가진 Element 클래스 생성
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

 # name, symbol, number 속성의 값을 출력하는 dump() 메서드

   # def dump(self):
   #     print(self.name, self.symbol, self.number)

# __str__() 메서드로 바꾸기
    def __str__(self):
         return f'{self.name} {self.symbol} {self.number}'

# 'name' : 'Hydrogen', 'symbol' : 'H', 'number' : 1과 같이
#  키와 값으로 이루어진 el_dict 딕셔너리 생성

el_dict = {'name' : 'Hydrogen', 'symbol' : 'H', 'number' : 1}

# el_dict 딕셔너리로부터 Element 클래스의 hydrogen 객체를 생성

hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
print(hydrogen.name, hydrogen.symbol, hydrogen.number)

# hydrogen.dump()

hydrogen.__str__()

# dump() 메서드 일 때 print(hydrogen) 호출 결과 : <__main__.Element object at 0x000001BF8488CB90>
# __str__() 메서드 일 때 print(hydrogen) 호출 결과 : Hydrogen H 1
print(hydrogen)