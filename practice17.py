#메소드 오버라이딩

#일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}"\
            .format(self.name, location, self.speed))


#공격 유닛
class AttackUnit(Unit): #상속() AttackUnit은 일반 유닛에서 상속받음

    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):#메소드
        print("{0} : {1} 적군을 공격. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):#메소드
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))        

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): #AttackUnit, Flyable 2개를 상속(다중 상속)받고 초기화
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable. __init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)    

vulture = AttackUnit("벌쳐", 80, 10, 20)

battlecrusier = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecrusier.fly(battlecrusier.name, "9시")
battlecrusier.move("9시")