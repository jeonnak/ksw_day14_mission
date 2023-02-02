"""
10.9
세 클래스 Bear, Rabbit, Octothorpe를 정의해보자.
각 클래스에 eats() 메서드를 정의해보자.
각 메서드는 'berries' (Bear), 'clover' (Rabbit), 'campers' (Octothorpe)를
반환한다. 각 클래스의 객체를 생성하고, eats() 메서드의 반환값을 출력한다.
"""

class Bear():
    def __init__(self, berries):
        self.berries = berries

    def eats(self):
        print(f'{self.berries}')

food = Bear('berries')
food.eats()

class Rabbit():
    def __init__(self, clover):
        self.clover = clover

    def eats(self):
        print(f'{self.clover}')

food = Rabbit('clover')
food.eats()

class Octothorpe():
    def __init__(self, campers):
        self.campers = campers

    def eats(self):
        print(f'{self.campers}')

food = Octothorpe('campers')
food.eats()