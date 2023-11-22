#클래스
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self,name))
        print("체력 {0}, 공격력{1}".format(self.hp, self.damage))

#공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
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

firebat1 = AttackUnit("파이어뱃", 50, 15)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)



