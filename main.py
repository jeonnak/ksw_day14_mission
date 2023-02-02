"""
10.1 아무 내용이 없는 Thing 클래스를 만들어서 출력한다.
이 클래스의 example 객체를 생성해서 출력한다.
이때 두 출력값은 같은가?
"""

# 아무 내용이 없는 Thing 클래스 생성
class Thing():
    pass

# Thing 클래스 출력
print(Thing)

# Thing 클래스의 example 객체 생성
example = Thing()

# example 객체 출력
print(example)

"""
10.2 Thing2 클래스를 만들고 이 클래스의 letters 속성에 값 'abc'를
할당한 후 letters를 출력해보자.
"""

# Thing2 클래스 생성
class Thing2():

    # letters 속성에 값 'abc'할당
    letters = 'abc'

# 출력
print(Thing2)


"""
10.3 Thing3 클래스를 만든다. 이번에는 인스턴스(객체)의 letters 속성에
값 'xyz'를 할당한 후 letters를 출력한다.
letters를 출력하기 위해 객체를 생성해야 하는가?
"""

class Thing3():
    def __init__(self):
        self.letters = 'xyz'
example = Thing3()
print(example.letters)
