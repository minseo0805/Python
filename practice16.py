#일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


#공격 유닛
class AttackUnit(Unit): #상속() AttackUnit은 일반 유닛에서 상속받음

    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
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
        AttackUnit.__init__(self, name, hp, damage)
        Flyable. __init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")