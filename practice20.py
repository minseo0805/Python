class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()  #맨처음에 상속받는 생성자만 초기화, 호출됨
        # Unit. __init__(self)
        # Flyable. __init__(self)  #둘다 초기화 하고싶으면 이방법 사용

dropship = FlyableUnit()